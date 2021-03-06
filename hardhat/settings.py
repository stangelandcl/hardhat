import datetime
import multiprocessing
import os
import platform
from .util import Object, run_or_error
from .config import ConfigParser, read_config

DEFAULT = 'hardhat'
_now = datetime.datetime.now()
TARGET = _now.date().isoformat().replace('-', '') \
        + str(chr(ord('a') + _now.hour))


def make_target_triplet(arch, os_name):
    return '%s-%s-%s-gnu' % (arch, TARGET, os_name)


def get_target_triplet(arch, os_name):
    target = os.environ.get('HARDHAT_TARGET')
    target = target if target else make_target_triplet(arch, os_name)
    os.environ['HARDHAT_TARGET'] = target
    return target


def get_use_root(use_root):
    return os.environ.get('HARDHAT_USE_ROOT', 'yes' if use_root else 'no') \
        == 'yes'


def get_march():
    target = os.environ.get('HARDHAT_MARCH')
    target = target if target else 'core2'
    os.environ['HARDHAT_MARCH'] = target
    return target


def root_target_triplet():
    return run_or_error(['/usr/bin/gcc', '-dumpmachine'],
                        '/tmp', {}).strip()


class RecipeSettings(Object):
    quiet = False
    silent = False

    def __init__(self, *args, **kwargs):
        super(RecipeSettings, self).__init__(*args, **kwargs)
        self.parser = ConfigParser()

        arch = platform.machine()
        os_name = platform.system().lower()
        self.arch = arch
        self.os_name = os_name
        self.host_triplet = get_target_triplet(arch, os_name)
        self.target_triplet = self.host_triplet
        self.build_triplet = '%s-unknown-%s-gnu' % (arch, os_name)
        self.tarball_dir = os.path.expanduser('~/Downloads/hardhat')
        self.march = get_march()
        self.post_clean = True
        self.no_sudo = False
        self.mingw64 = False
        self.use_root = False

        self.prefix_dir = os.path.expanduser('~/hardhat')
        self.quiet = RecipeSettings.quiet
        self.silent = RecipeSettings.silent
        self.installer = None
        self.enable_version_check = False

        self.tmp_dir = os.path.join(self.prefix_dir, 'tmp')

        if 'settings' in kwargs:
            self._copy_settings(kwargs['settings'])

    def _copy_settings(self, src):
        self.use_root = src.use_root
        self.host_triplet = src.host_triplet
        self.target_triplet = src.target_triplet
        self.tarball_dir = src.tarball_dir
        self.prefix_dir = src.prefix_dir
        self.quiet = src.quiet
        self.silent = src.silent
        self.tmp_dir = src.tmp_dir
        self.cpu_count = src.cpu_count
        if hasattr(src, 'install_file'):
            self.install_file = src.install_file
        self.installer = src.installer
        self.march = src.march
        self.post_clean = src.post_clean
        self.enable_version_check = src.enable_version_check
        self.no_sudo = src.no_sudo
        self.mingw64 = src.mingw64
#        self.settings_filename = src.settings_filename

    ## @property
    ## def build_triplet(self):
    ##     if not hasattr(self, '_build_triplet'):
    ##         self._build_triplet = run(['gcc', '-dumpmachine'],
    ##                                   os.path.expanduser('~'),
    ##                                   self.environment).decode('utf-8').strip()
    ##     return self._build_triplet

    ## @build_triplet.setter
    ## def build_triplet(self, value):
    ##     self._build_triplet = value

    @property
    def cpu_count(self):
        if not hasattr(self, '_cpu_count'):
            return max(multiprocessing.cpu_count() - 1, 1)
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, value):
        self._cpu_count = value

    def load(self):
        if not os.path.exists(self.filename):
            return
        self._read()
        p = read_config(self.filename)
        self.cpu_count = p.getdefaultfloat(DEFAULT,
                                           'cpus',
                                           self.cpu_count)

    def save(self):
        self.parser.set(DEFAULT, 'cpus', self.cpu_count)
        with open(self.filename, 'wt') as f:
            self.parser.write(f)
