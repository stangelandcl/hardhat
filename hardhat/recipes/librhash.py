from .base import GnuRecipe


class LibRHashRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibRHashRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '964df972b60569b5cb35ec989ced195a' \
                      'b8ea514fc46a74eab98e86569ffbcf92'

        self.name = 'librhash'
        self.version = '1.3.6'
        self.url = 'https://github.com/rhash/RHash/archive/v$version.tar.gz'
        self.version_url = 'https://github.com/rhash/RHash/releases'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'

        self.compile_args = ['make',
                             'lib-static',
                             'lib-shared',
                             '-j%s' % self.cpu_count,
                             'PREFIX=""',
                             'DEST_DIR=%s' % self.prefix_dir]

        self.install_args += ['install-lib-shared',
                              'install-lib-static',
                              'PREFIX=""',
                              'DESTDIR=%s' % self.prefix_dir]

        self.configure_strip_cross_compile()
