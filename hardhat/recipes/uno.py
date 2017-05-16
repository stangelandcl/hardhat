import os
import shutil
from .base import GnuRecipe
from ..util import patch


class UnoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(UnoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c688a5f7c68ba4b7c0907c6c26037035' \
                      '35c37b99b2a3927a391bd48c43d7bcbe'

        self.name = 'uno'
        self.version = '2.13'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'http://www.spinroot.com/uno/uno_v%s.tar.gz' % (
            self.version.replace('.', ''))
        self.compile_args = ['make']

    def patch(self):
        self.old_dir = self.directory
        self.directory = os.path.join(self.directory, 'src')

        self.log_dir('patch', self.directory, 'patching makefile')
        src = 'BINDIR=/usr/bin/'
        dst = 'BINDIR=%s/bin/' % self.prefix_dir
        filename = os.path.join(self.directory, 'makefile')
        patch(filename, src, dst)

        src = 'CFLAGS=-ansi -Wall -m32'
        dst = 'CFLAGS=-ansi -Wall'
        patch(filename, src, dst)

    def configure(self):
        pass

    def install(self):
        super(UnoRecipe, self).install()

        self.log_dir('install', self.directory, 'installing docs')
        dst = os.path.join(self.prefix_dir, 'share', 'doc', self.name)
        if not os.path.exists(dst):
            os.makedirs(dst)

        src = ['uno_long.pdf', 'uno_man.pdf',
               'uno_manpage.pdf', 'uno_short.pdf']
        for s in src:
            src_file = os.path.join(self.old_dir, 'doc', s)
            dst_file = os.path.join(dst, s)
            shutil.copy2(src_file, dst_file)

        self.log_dir('install', self.directory, 'installing manpages')
        man_dst = os.path.join(
            self.prefix_dir, 'share', 'man', 'man1', 'uno.1')
        src = os.path.join(self.old_dir, 'doc', 'uno.1')
        shutil.copy2(src, man_dst)
