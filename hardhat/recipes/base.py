import os
import shutil
from string import Template
import subprocess
from hardhat.util import hash_file, matches_hash, Object, \
    open_file, read_process_async, save_url
from hardhat.environment import runtime_env, environment_strip_lto
from hardhat.tarball import Tarball
from hardhat.terminal import Terminal
from hardhat.settings import RecipeSettings
from hardhat.urls import Urls, GithubUrl, GithubProject
from hardhat.util import exception_str, runtime
from hardhat.version import Versions, version_compare

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class ExeRunner(Object):
    def __init__(self, *args, **kwargs):
        super(ExeRunner, self).__init__(*args, **kwargs)

    def run_exe(self, args, directory, environment):
        arg_str = args
        if isinstance(args, list):
            arg_str = ' '.join(args)
        p = subprocess.Popen(arg_str,
                             shell=True,
                             bufsize=1,
                             cwd=directory,
                             env=environment,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        output = []
        read_process_async(p.stdout, output)
        read_process_async(p.stderr, output)

        while True:
            p.poll()
            if p.returncode is not None:
                break
            lines = output[:]
            clear_list(output)
            for line in lines:
                self.log_verbose(line)

        rc = p.wait()
        if rc:
            raise Exception('%s in %s failed: %s' % (arg_str, directory, rc))


class Logger(Object):
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)

    @property
    def log_name(self):
        v = self.version
        if len(v) > 8:
            v = self.short_version
        return '%s-%s' % (self.name, v)

    @property
    def log_filename(self):
        if hasattr(self, '_log_filename'):
            return self._log_filename
        return os.path.join(self.prefix_dir, 'install.log')

    @log_filename.setter
    def log_filename(self, value):
        self._log_filename = value

    @property
    def log_file(self):
        if not hasattr(self, '_logfile'):
            self._logfile = open_file(self.log_filename, 'at', 'utf-8')
        return self._logfile

    def log_to_file(self, line):
        line = Terminal.strip(line)
        self.log_file.write(line + '\n')
        self.log_file.flush()

    def log_verbose(self, line):
        if not self.quiet and not self.silent:
            print(line)
        self.log_to_file(line)

    def log(self, stage, *args):
        stage = Terminal.normal_green(stage)

        name = Terminal.bold_white(self.log_name)
        text = '[%s: %s] %s' % (name, stage, ' '.join(str(x) for x in args))

        print(text)
        self.log_to_file(text)

    def log_warn(self, stage, *args):
        stage = Terminal.bold_red(stage)

        name = Terminal.bold_white(self.log_name)
        text = '[%s: %s] %s' % (name, stage, ' '.join(str(x) for x in args))

        print(text)
        self.log_to_file(text)

    def log_yellow(self, stage, *args):
        stage = Terminal.normal_yellow(stage)

        name = Terminal.bold_white(self.log_name)
        text = '[%s: %s] %s' % (name, stage, ' '.join(str(x) for x in args))

        print(text)
        self.log_to_file(text)

    def log_dir(self, stage, dir, *args):
        stage = Terminal.normal_green(stage)

        name = Terminal.bold_white(self.log_name)
        dir = Terminal.light_white('(%s)' % (dir))
        text = '[%s: %s %s] %s %s' % (name,
                                      stage,
                                      runtime(),
                                      dir,
                                      ' '.join(str(x) for x in args))

        print(text)
        self.log_to_file(text)


class EmptyRecipe(Object):
    def __init__(self, *args, **kwargs):
        super(EmptyRecipe, self).__init__(*args, **kwargs)
        self.depends = []

    @property
    def provides(self):
        return [self.name]

    def run(self):
        pass


class ShortVersionMixin(Object):
    def __init__(self, *args, **kwargs):
        super(ShortVersionMixin, self).__init__(*args, **kwargs)

    @property
    def short_version(self):
        version = self.version
        if len(version) == 40:  # git commit hash
            version = version[:8]
        elif '.' in version:
            version = '.'.join(version.split('.')[:2])
        return version


class GetVersionMixin(Object):
    def __init__(self, *args, **kwargs):
        super(GetVersionMixin, self).__init__(*args, **kwargs)

    @property
    def version_regex(self):
        if hasattr(self, '_version_regex'):
            return self._version_regex
        return Versions.default_regex(self.version_prefix)

    @version_regex.setter
    def version_regex(self, value):
        self._version_regex = value

    @property
    def version_prefix(self):
        if hasattr(self, '_version_prefix'):
            return self._version_prefix
        return self.name

    @version_prefix.setter
    def version_prefix(self, value):
        self._version_prefix = value

    @property
    def version_url(self):
        if hasattr(self, '_version_url'):
            return self._version_url
        if isinstance(self.url, GithubUrl):
            return self.url
        return Urls.drop_file(self.url)

    @version_url.setter
    def version_url(self, value):
        self._version_url = value

    def get_version(self):
        v = str(self.version_url)
        if 'sourceforge.net' in v:
            return Versions.scrape_page(self.version_url, self.version_regex)
        elif ('github.com' not in v or hasattr(self, '_version_url')):
            return Versions.get_from_directory(
                self.version_url, self.version_regex)
        elif isinstance(self.version_url, GithubUrl):
            return Versions.scrape_page(self.version_url.project.releases_url,
                                        self.version_regex)
        return (None, None)

    def version_check(self):
        try:
            v, has_multiple = self.get_version()
            if not v:
                self.log_yellow(
                    'version_check', self.name + ' ' + self.version,
                    'skipped')
            elif self.version_compare(v) > 0:
                self.log_warn('version_check', 'new version available: %s > %s'
                              % (Terminal.bold_red(v), self.version))
            elif has_multiple:
                self.log_dir('version_check', self.name + ' ' + self.version,
                             'up to date')
            else:
                self.log_yellow('version_check',
                                self.name + ' ' + self.version,
                                'maybe up to date. only one version found.')
        except Exception as e:
            text = str(e)
            if not text.startswith('HTTP Error '):
                text = exception_str(e)
            self.log_yellow('version_check', 'check failed: %s' % text)

    def version_compare(self, new_version):
        new_version = self.version_transform(new_version)
        return version_compare(new_version, self.version)

    def version_transform(self, new_version):
        return new_version


class Recipe(RecipeSettings, Logger, ExeRunner, ShortVersionMixin):
    def __init__(self, *args, **kwargs):
        super(Recipe, self).__init__(*args, **kwargs)
        self.depends = []
        if not hasattr(self, 'sha256'):
            self.sha256 = None
        self.environment = runtime_env(self.prefix_dir,
                                       self.target_triplet,
                                       self.tarball_dir)
        self.directory_template = '$prefix/build/$name-$version'

    @property
    def directory(self):
        if hasattr(self, '_directory'):
            return self._directory
        return Template(self.directory_template).substitute(
            name=self.name,
            prefix=self.prefix_dir,
            version=self.short_version)

    @directory.setter
    def directory(self, value):
        self._directory = value

    def environment_strip_lto(self):
        environment_strip_lto(self.environment)

    @property
    def shell_args(self):
        if not hasattr(self, '_shell_args'):
            return ['/bin/bash',
                    '--noprofile',
                    '--norc'
                    ]
        return self._shell_args

    @shell_args.setter
    def shell_args(self, value):
        self._shell_args = value

    def init(self):
        dirs = [self.prefix_dir,
                self.tarball_dir,
                self.tmp_dir]

        for dir in dirs:
            if not os.path.exists(dir):
                os.makedirs(dir)

    @property
    def provides(self):
        return [self.name]

    def version_check(self):
        pass

    def clean(self):
        pass

    def download(self):
        pass

    def extract(self):
        pass

    def patch(self):
        """post-extract"""
        pass

    def configure(self):
        pass

    def compile(self):
        pass

    def test(self):
        """post-compile"""
        pass

    def install(self):
        pass

    def post_install(self):
        # run ldconfig to rebuild ld cache
        args = ['ldconfig']
        dir = os.path.join(self.prefix_dir, self.target_triplet, 'etc')
        self.log_dir('post-install', dir, 'ldconfig')
        self.run_exe(args, dir, self.environment)

    def run(self):
        self.init()
        self.version_check()
        self.download()
        self.extract()
        self.patch()
        self.configure()
        self.compile()
        self.install()
        self.post_install()


def clear_list(x):
    del x[:]


class Patcher(Object):
    def __init__(self, *args, **kwargs):
        super(Patcher, self).__init__(*args, **kwargs)

    def apply_patch(self, directory, patch_text):
        patch_file = os.path.join(directory, 'patch1.patch')
        self.log_dir('patch', self.directory, 'writing patch1.patch')
        with open_file(patch_file, 'wt', encoding='utf-8') as f:
            f.write(patch_text)
        args = ['patch',
                '--forward',
                '--strip=1',
                '--input=patch1.patch']
        self.log_dir('patch', directory, ' '.join(args))
        self.run_exe(args, directory, self.environment)


class Downloader(Object):
    def __init__(self, *args, **kwargs):
        super(Downloader, self).__init__(*args, **kwargs)

        # add to settings. disable on bootstrap. enable afterwards
        self.verify_ssl_certificate = True
        self.extra_downloads = []

    def _is_already_download(self, filename, sha256):
        if not sha256 or not os.path.exists(filename):
            return False
        return hash_file(filename) == sha256

    def _check_hash(self, filename, sha256):
        h = hash_file(filename)
        if sha256:
            if sha256 != h:
                raise Exception("Hash mismatch for %s: %s != %s"
                                % (filename, sha256, Terminal.bold_red(h)))
        else:
            name = os.path.basename(filename)
            if name.endswith('.tmp'):
                name = name[:-4]
            h = Terminal.bold_red(h)
            self.log('download', 'sha256 of %s =\n' \
                     "        self.sha256 = '%s' \\\n         " \
                     "             '%s'" % (name, h[:39], h[39:]))

    @property
    def url(self):
        if isinstance(self._url, GithubUrl):
            return self._url
        return Template(self._url).substitute(
            name=self.name,
            version=self.version)

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def filename(self):
        if not hasattr(self, '_filename'):
            directory = self.tarball_dir
            u = urlparse(self.url)
            filename = os.path.basename(u.path)
            filename = os.path.join(directory, filename)
            return filename
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def github_commit(self, user, name=None):
        if not name:
            name = self.name
        return Urls.github_commit(user, name, self.version)

    def do_download(self, tmpfile):
        save_url(self.url, tmpfile, self.verify_ssl_certificate)

    def download(self):
        filename = self.filename

        if not self._is_already_download(filename, self.sha256):
            tmpfile = filename + '.tmp'
            exists = os.path.exists(tmpfile)
            if not exists or hash_file(tmpfile) != self.sha256:
                if not self.quiet and not self.silent:
                    self.log('download', 'from ' + self.url)
                self.log('download', '%s to %s' % (self.url, filename))
                self.do_download(tmpfile)
                self._check_hash(tmpfile, self.sha256)
            os.rename(tmpfile, filename)
        for extra in self.extra_downloads:
            downloader = LogDownloader(settings=self)
            downloader.name = extra.name
            downloader.version = extra.version
            downloader.environment = self.environment
            downloader.url = extra.url
            downloader.sha256 = extra.sha256
            downloader.download()
            extra.filename = downloader.filename


class Extractor(Object):
    def __init__(self, *args, **kwargs):
        super(Extractor, self).__init__(*args, **kwargs)
        self.extract_dir_template = '$base_extract_dir/$name-$version'

    @property
    def base_extract_dir(self):
        if hasattr(self, '_base_extract_dir'):
            return self._base_extract_dir
        return '%s/build' % (self.prefix_dir)

    @base_extract_dir.setter
    def base_extract_dir(self, value):
        self._base_extract_dir = value

    @property
    def extract_dir(self):
        if hasattr(self, '_extract_dir'):
            return self._extract_dir
        return Template(self.extract_dir_template).substitute(
            base_extract_dir=self.base_extract_dir,
            name=self.name,
            version=self.short_version)

    @extract_dir.setter
    def extract_dir(self, value):
        self._extract_dir = value

    def clean(self):
        dir = self.extract_dir
        if os.path.exists(dir):
            self.log_dir('clean', dir, '')
            shutil.rmtree(dir)

    def extract(self):
        if not os.path.exists(self.extract_dir):
            filename = self.filename
            self.log_dir('extract', self.extract_dir, '%s' % (filename))
            with Tarball(filename) as f:
                f.extract(self.extract_dir)

    def extract_into(self, filename, directory):
        '''Extra into existing directory'''
        args = ['tar', 'xf', filename, '-C',
                directory]
        self.log_dir('extract', directory,
                     'extract %s' % filename)
        self.run_exe(args, directory, self.environment)


class Configure(Object):
    def __init__(self, *args, **kwargs):
        super(Configure, self).__init__(*args, **kwargs)


    @property
    def configure_args(self):
        if not hasattr(self, '_configure_args'):
            return self.shell_args + \
                ['./configure',
                 '--prefix=%s' % (self.prefix_dir),
                 '--build=%s' % (self.build_triplet),
                 '--host=%s' % (self.host_triplet),
#                 '--with-sysroot=%s' % self.prefix_dir
                ]
        return self._configure_args

    @configure_args.setter
    def configure_args(self, value):
        self._configure_args = value

    def configure_directory(self):
        return self.directory

    def need_configure(self):
        directory = self.configure_directory()
        makefile = os.path.join(directory, 'Makefile')
        files = ['configure', 'config', 'Config', 'Configure', 'setup.py',
                 'CMakeLists.txt']
        if not os.path.exists(makefile):
            return True
        for file in files:
            f = os.path.join(self.directory, file)
            if os.path.exists(f):
                return True
        return False

    def configure_strip_cross_compile(self):
        self.configure_args = list(filter(lambda x:
                                          not x.startswith('--build=')
                                          and not x.startswith('--host='),
                                          self.configure_args))

    def configure_strip_sysroot(self):
        self.configure_args = list(filter(lambda x:
                                          not x.startswith('--with-sysroot='),
                                          self.configure_args))


    def configure(self):
        directory = self.configure_directory()

        if not self.need_configure():
            self.log_dir('configure', directory, 'Skip')
            return

        args = self.configure_args
        if not isinstance(self.configure_args[0], list):
            args = [self.configure_args]

        for arg_list in args:
            self.log_dir('configure', directory, '%s' %
                         (' '.join(arg_list)))

#        print('config=', self.configure_args)
#        print('directory=', directory)
#        print('env=', self.environment)
            self.run_exe(arg_list,
                         directory,
                         self.environment)
#        self.log('configure', 'Success')


class Make(Object):
    def __init__(self, *args, **kwargs):
        super(Make, self).__init__(*args, **kwargs)
        self.compile_args = ['make',
                             '-j%s' % (self.cpu_count)
                             ]

    def compile_directory(self):
        return self.directory

    def need_compile(self):
        return True

    def compile(self):
        if not self.need_compile():
            return False

        directory = self.compile_directory()

        if isinstance(self.compile_args[0], list):
            args = self.compile_args
        else:
            args = [self.compile_args]
        for arg_set in args:
            self.log_dir('compile', directory, '%s' %
                         (' '.join(arg_set)))

            self.run_exe(arg_set,
                         directory,
                         self.environment)


class MakeInstall(Object):
    def __init__(self, *args, **kwargs):
        super(MakeInstall, self).__init__(*args, **kwargs)
        self.install_args = ['make',
                             'install']

    def install_directory(self):
        return self.directory

    def install(self):
        directory = self.install_directory()

        if isinstance(self.install_args[0], list):
            args = self.install_args
        else:
            args = [self.install_args]

        for arg_list in args:
            cmd = ' '.join(arg_list)
            self.log_dir('install', directory, cmd)
            self.run_exe(arg_list,
                         directory,
                         self.environment)


class TarballRecipe(Downloader, Extractor, GetVersionMixin, Recipe):
    def __init__(self, *args, **kwargs):
        super(TarballRecipe, self).__init__(*args, **kwargs)

    def configure(self):
        directory = self.directory
        self.log_dir('configure', directory, '%s' %
                     (' '.join(self.configure_args)))

#        print('config=', self.configure_args)
#        print('directory=', directory)
#        print('env=', self.environment)
        self.run_exe(self.configure_args,
                     directory,
                     self.environment)

    def install_directory(self):
        return self.directory

    def install(self):
        directory = self.install_directory()

        self.log_dir('install', directory, '%s' % (self.prefix_dir))
        self.run_exe(self.install_args,
                     directory,
                     self.environment)


class GnuRecipe(Configure, Make, MakeInstall, Patcher, TarballRecipe,
                ShortVersionMixin):
    def __init__(self, *args, **kwargs):
        super(GnuRecipe, self).__init__(*args, **kwargs)


class LogConfigure(Configure, Logger, ExeRunner, ShortVersionMixin):
    def __init__(self, *args, **kwargs):
        super(LogConfigure, self).__init__(*args, **kwargs)


class LogDownloader(Downloader, Logger, ShortVersionMixin, RecipeSettings):
    def __init__(self, *args, **kwargs):
        super(LogDownloader, self).__init__(*args, **kwargs)


class LogExtractor(Extractor, Logger, ShortVersionMixin):
    def __init__(self, *args, **kwargs):
        super(LogExtractor, self).__init__(*args, **kwargs)


class LogMakeInstall(MakeInstall, Logger, ExeRunner, ShortVersionMixin):
    def __init__(self, *args, **kwargs):
        super(LogMakeInstall, self).__init__(*args, **kwargs)
