import os
from .base import GnuRecipe


class LibSmb2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSmb2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '97ce9cce181fc24e30a795b3a3d18f00' \
                      'da9923599477f7dae64a0ea8305494a5'
        self.description = 'SMB 2/3 library'
        self.name = 'libsmb2'
        self.depends = ['autotools', 'mit-kerberos']
        self.version = '2.0.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/sahlberg/libsmb2/releases'
        self.url = 'https://github.com/sahlberg/libsmb2/archive/' \
                   'v$version.tar.gz'
        self.configure_args = self.cmake_args + ['..']

    def configure(self):
        dir = os.path.join(self.directory, 'build')
        self.directory = dir
        os.makedirs(self.directory)
        super(LibSmb2Recipe, self).configure()
