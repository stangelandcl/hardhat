from .base import GnuRecipe


class CmakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CmakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c53d5c2ce81d7a957ee83e3e635c8cda' \
                      '5dfe20c9d501a4828ee28e1615e57ab2'
        self.name = 'cmake'
        self.version = '3.12.1'
        self.depends = ['bzip2', 'curl', 'expat', 'jsoncpp',
                        'libarchive', 'librhash', 'libuv',
                        'xz', 'zlib']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://www.cmake.org/files/v%s/' \
                   'cmake-$version.tar.gz' % short_version
        self.version_url = 'https://github.com/Kitware/CMake/releases'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
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
            '--no-qt-gui',
            '--no-system-librhash',
            ]
