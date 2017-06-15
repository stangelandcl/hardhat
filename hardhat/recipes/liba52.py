import os
import shutil
from .base import GnuRecipe


class LibA52Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibA52Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a21d724ab3b3933330194353687df82c' \
                      '475b5dfb997513eef4c25de6c865ec33'

        self.name = 'liba52'
        self.version = '0.7.4'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://liba52.sourceforge.net/files/a52dec-$version.tar.gz'
        self.configure_args += ['--enable-shared']
        self.environment['CFLAGS'] += ' -fPIC'

    def install(self):
        super(LibA52Recipe, self).install()

        self.log_dir('install', self.directory, 'copy internal header')
        src = os.path.join(self.directory, 'liba52', 'a52_internal.h')
        dst = os.path.join(self.prefix_dir,
                           'include', 'a52dec', 'a52_internal.h')
        shutil.copy2(src, dst)

        src = os.path.join(self.directory, 'doc', 'liba52.txt')
        dst = os.path.join(self.prefix_dir, 'share', 'doc', 'liba52.txt')

        shutil.copy2(src, dst)
