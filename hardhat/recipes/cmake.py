from .base import GnuRecipe


class CmakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CmakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ce5d9161396e06501b00e52933783150' \
                      'a87c33080d4bdcef461b5b7fd24ac228'

        self.name = 'cmake'
        self.version = '3.8.1'
        self.depends = ['bzip2', 'curl', 'expat', 'jsoncpp',
                        'libarchive', 'librhash', 'libuv',
                        'xz', 'zlib']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://www.cmake.org/files/v%s/' \
                   'cmake-$version.tar.gz' % short_version
 #       self.configure_strip_cross_compile()
#        self.environment_strip_lto()
#        self.environment['CFLAGS'] = ''
#        self.environment['CXXFLAGS'] = self.environment['CFLAGS']
        self.environment['CXXFLAGS'] += ' -Wno-odr'
        self.configure_args = self.shell_args + [
            'bootstrap',
            '--prefix=%s' % self.prefix_dir,
            '--parallel=%s' % self.cpu_count,
            '--system-libs',
            '--no-system-jsoncpp',
            '--no-qt-gui'
            ]
