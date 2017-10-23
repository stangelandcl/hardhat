import datetime
from errno import EACCES, EPERM
import hashlib
import importlib
import inspect
import os
import shutil
import ssl
import stat
import sys
import subprocess
import traceback
from threading import Thread

try:
    from urllib.request import urlopen, ProxyHandler, build_opener, \
        install_opener
except ImportError:
    from urllib2 import urlopen, ProxyHandler, build_opener, install_opener

http_proxy = os.environ.get('http_proxy', os.environ.get('HTTP_PROXY'))
https_proxy = os.environ.get('https_proxy', os.environ.get('HTTPS_PROXY'))

if http_proxy or https_proxy:
    proxy = dict()
    if http_proxy:
        proxy['http'] = http_proxy
    if https_proxy:
        proxy['https'] = https_proxy

    proxyHandler = ProxyHandler(proxy)
    proxyOpener = build_opener(proxyHandler)
    install_opener(proxyOpener)

START_TIME = datetime.datetime.now()


def timedelta_total_seconds(timedelta):
    # from stackoverflow. For Python < 2.7
    # otherwise timedelta.total_seconds() would work
    return (
        timedelta.microseconds + 0.0 +
        (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6


def runtime():
    now = datetime.datetime.now()
    span = (now - START_TIME)
    span = timedelta_total_seconds(span)
    hours = int(span / 60 / 60)
    span -= hours * 60 * 60
    minutes = int(span / 60)
    span -= minutes * 60
    sec = int(span)
    return '%02d:%02d:%02d' % (hours, minutes, sec)

_gcc_version = (0, 0, 0)
_gcc_exe = None
def gcc_version(exe):
    global _gcc_version, _gcc_exe
    if not _gcc_exe or exe != _gcc_exe:
        text = run_or_error([exe, '--version'], '/tmp', {})
        version = text.strip().split('\n')[0].split(' ')[2]
        v = version.split('.')
        _gcc_exe = exe
        _gcc_version = (int(v[0]), int(v[1]), int(v[2]))
    return _gcc_version

def open_file(filename, mode, encoding):
    if sys.version_info[0] == 2:
        return open(filename, mode)
    return open(filename, mode, encoding=encoding)


def create_ssl_context(verify=True):
    if sys.version_info[0] == 2 and sys.version_info[1] <= 6:
        return None

    ctx = None
    if not verify:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    return ctx


def read_url(url, verify=True):
    if sys.version_info[0] == 2 and sys.version_info[1] <= 6:
        return urlopen(url).read()
    else:
        ctx = create_ssl_context(verify)
        return urlopen(url, context=ctx).read()


def save_url(url, filename, verify=True):
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(filename, 'wb') as f:
        if sys.version_info[0] == 2 and sys.version_info[1] <= 6:
            req = urlopen(url)
        else:
            ctx = create_ssl_context(verify)
            req = urlopen(url, context=ctx)
        shutil.copyfileobj(req, f)


def read_process(stdout, output):
    while True:
        line = stdout.readline()
        if not line:
            break
        try:
            # just ignore non-utf-8 output
            text = line.decode('utf-8').strip()
        except:
            text = ''
        output.append(text)


def read_process_async(stdout, output):
    t = Thread(target=read_process, args=(stdout, output))
    t.daemon = True
    t.start()
    return t


# Base class because object.__init__() errors when passed **kwargs
class Object(object):
    def __init__(self, *args, **kwargs):
        pass


def check_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def matches_hash(filename, sha256):
    """Check if file exists and matches the hash code"""
    if not os.path.exists(filename):
        return False
    return sha256 == hash_file(filename)


def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            x = f.read(4096)
            if not x:
                break
            h.update(x)
    return h.hexdigest()


def run(args, cwd, env):
    with open('/dev/null', 'w') as f:
        return subprocess.Popen(' '.join(args),
                                shell=True,
                                cwd=cwd,
                                stdout=subprocess.PIPE,
                                stderr=f,
                                env=env).communicate()[0].decode('utf-8')


def run_or_error(args, cwd, env):
    cmd = ' '.join(args)
    p = subprocess.Popen(cmd,
                         shell=True,
                         cwd=cwd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         env=env)
    text, errs = p.communicate()
    text = text.decode('utf-8')
    errs = errs.decode('utf-8')

    if p.returncode:
        raise Exception('Error running command: %s. Error %s: %s' %
                        (cmd, p.returncode, errs))
    return text


def load_recipes(directory, prefix, exclusions=['__init__.py', 'base.py']):
    recipes = []
    for root, dirs, files in os.walk(directory):
        files.sort()
        for filename in files:
            if filename in exclusions:
                continue
            filename, ext = os.path.splitext(filename)
            if ext != '.py':
                continue
            modulename = '%s.%s' % (prefix, filename)
#            print('importing ' + modulename)
            module = importlib.import_module(modulename)
            members = inspect.getmembers(module, inspect.isclass)
            for name, member in members:
                if (member.__module__ == modulename
                    and member.__name__.endswith('Recipe')):
                    recipes.append(member)

        break
    return recipes


def add_dependencies(settings, dependencies, recipes):
    for recipe in recipes:
        recipe = recipe(settings=settings)
        exists = False
        for d in dependencies:
            if d[0] == recipe.name:
                exists = True
                break
        if not exists:
            d = [recipe.name] + recipe.depends
            dependencies.append(d)


def get_groups():
    groups = []
    try:
        groups = os.getgroups()
    except:
        groups = [os.environ['USER']]
    return groups


def is_file_open(filename):
    # Like on Windows
    if not os.path.exists('/proc'):
        return False

    filename = os.path.normpath(filename)
    root, dirs, files = next(os.walk('/proc'))
    for dir in dirs:
        try:
            id = int(dir)
        except ValueError:
            continue

        if id == os.getpid():
            continue

        dir = os.path.join('/proc', dir)
        fd_dir = os.path.join(dir, 'fd')
        if not os.path.exists(fd_dir):
            continue

        try:
            with open(os.path.join(dir, 'cmdline'), 'rt') as f:
                cmdline = f.read()
                if 'hardhat' not in cmdline:
                    continue
        except Exception as e:
            pass

        dir = fd_dir
        files = listdir(dir)

        for file in files:
            file = os.path.join(dir, file)
            path = os.path.normpath(os.path.realpath(file))
            if path == filename:
                return True
    return False


def listdir(dir):
    if sys.version_info[0] < 3 or sys.version_info[1] < 3:
        try:
            return os.listdir(dir)
        except Exception as e:
            if hasattr(e, 'errno') and (e.errno == EPERM or e.errno == EACCES):
                return []
    else:
        try:
            return os.listdir(dir)
        except PermissionError:
            return []


def patch(filename, find, replace):
    with open_file(filename, 'rt', encoding='utf-8') as f:
        text = f.read()
    if find not in text:
        raise Exception("Could not find: %s in %s to patch file"
                        % (find, filename))
    text = text.replace(find, replace)
    with open_file(filename, 'wt', encoding='utf-8') as f:
        f.write(text)


def exception_str(e):
    if hasattr(e, '__traceback__'):
        e_traceback = traceback.format_exception(e.__class__, e,
                                                 e.__traceback__)
        return str(e) + '\n' + ''.join(e_traceback)
    else:
        return str(e)


def make_executable(filename):
    os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
