import os
import shutil
from .base import GnuRecipe


class MemcacheppRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MemcacheppRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '481d587379f110417a08b88d13575dda' \
                      '53d99d80ef6a503934cd4e63b2fa4c87'

        self.name = 'memcachepp'
        self.version = 'e948be5189c1b8863bb4bfc6cf3830482933b54a'
        self.url = 'https://github.com/deanberris/memcachepp/archive/' \
                   '$version.tar.gz'
        self.depends = ['boost']
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_VERBOSE_MAKEFILE=ON']

    def install(self):
        self.log_dir('install', self.directory, 'copying headers')
        src = os.path.join(self.directory, 'memcachepp')
        dst = os.path.join(self.prefix_dir, 'include', 'memcachepp')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
