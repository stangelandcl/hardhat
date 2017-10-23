from .base import GnuRecipe


class LastPassCliRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LastPassCliRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1a49a37a67a973296e218306e6d36c93' \
                      '83347b1833e5a878ebc08355b1c77456'

        self.name = 'lastpass-cli'
        self.version = '1.2.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['asciidoc', 'cmake',
                        'curl', 'libxml2', 'openssl', 'pinentry']
        self.url = 'https://github.com/lastpass/lastpass-cli/archive/' \
                   'v$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '.'
            ]
        self.compile_args += ['doc-man', 'all']
        self.install_args += ['install-doc']
