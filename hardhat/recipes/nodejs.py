from .base import GnuRecipe


class NodeJsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NodeJsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b17071109238295b9f363b768afdff97' \
                      'a9f386203d4f080c91847ce76d4f7e93'

        self.name = 'nodejs'
        self.version = '8.6.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['c-ares', 'icu', 'openssl', 'python2']
        self.url = 'https://nodejs.org/dist/v$version/node-v$version.tar.xz'
        self.configure_args += ['--shared-cares',
                                '--shared-openssl',
                                '--shared-zlib',
                                '--with-intl=system-icu']
        self.configure_strip_cross_compile()
