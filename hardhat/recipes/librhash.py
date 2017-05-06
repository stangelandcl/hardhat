from .base import GnuRecipe


class LibRHashRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibRHashRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1f6daa0c066c94d2575f0aace76f34e5' \
                      '800c51f59f4b30029ddcfa9799564f98'

        self.name = 'librhash'
        self.version = '1.3.4'
        self.url = 'https://github.com/rhash/RHash/archive/v$version.tar.gz'

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
