import os
import shutil
import stat
from .base import GnuRecipe
from ..version import extension_regex


class BeyondLinuxFromScratchRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BeyondLinuxFromScratchRecipe, self).__init__(*args, **kwargs)
        self.name = 'blfs'
        self.version_regex = r'blfs-book-svn-html-' \
            '(?P<version>\d+-\d+-\d+)' + extension_regex
        self.version_url = 'http://www.linuxfromscratch.org/blfs/downloads/' \
                           'systemd/'
        self.url = 'http://www.linuxfromscratch.org/blfs/downloads/svn/' \
                   'blfs-book-svn-html-$version.tar.bz2'
        # call get_version() after setting other properties
        self.version = self.get_version()[0]
        if not self.version:
            self.version = '2017-05-08'
#            raise Exception('No version for BLFS found')

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'creating blfs')
        blfs = r'''#!/bin/sh
firefox ${HARDHAT_PREFIX}/doc/blfs/index.html
'''
        filename = os.path.join(self.prefix_dir, 'bin', 'blfs')
        with open(filename, 'wt') as f:
            f.write(blfs)
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)

        doc_dir = os.path.join(self.prefix_dir, 'doc', 'blfs')
        self.log_dir('install', doc_dir, 'installing')
        if os.path.exists(doc_dir):
            shutil.rmtree(doc_dir)
        shutil.copytree(self.directory, doc_dir)
