from .base import GnuRecipe


class ChickenSchemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChickenSchemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e3dc2b8f95b6a3cd59c85b5bb6bdb2bd' \
                      '9cefc45b5d536a20cad74e3c63f4ad89'

        self.name = 'chicken-scheme'
        self.description = "Chicken Scheme"
        self.version = '4.11.0'
        self.url = 'https://code.call-cc.org/releases/$version/' \
                   'chicken-$version.tar.gz'

        self.compile_args += ['PLATFORM=linux',
                              'PREFIX=%s' % self.prefix_dir]

        self.install_args += ['PLATFORM=linux',
                              'PREFIX=%s' % self.prefix_dir]
