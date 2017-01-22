import os
from .base import GnuRecipe


class CmakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CmakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '92d8410d3d981bb881dfff2aed466da5' \
                      '5a58d34c7390d50449aa59b32bb5e62a'

        self.name = 'cmake'
        self.version = '3.5.2'
        self.depends = ['bzip2', 'curl', 'expat', 'jsoncpp',
                        'libarchive', 'xz', 'zlib']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://www.cmake.org/files/v%s/' \
                   'cmake-$version.tar.gz' % short_version
 #       self.configure_strip_cross_compile()
#        self.environment_strip_lto()
#        self.environment['CFLAGS'] = ''
#        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.configure_args = self.shell_args + [
            'bootstrap',
            '--prefix=%s' % self.prefix_dir,
            '--parallel=%s' % self.cpu_count,
            '--system-libs',
            '--no-system-jsoncpp',
            '--no-qt-gui'
            ]
