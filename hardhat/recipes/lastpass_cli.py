from .base import GnuRecipe


class LastPassCliRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LastPassCliRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '26c93ae610932139dacaff2e0f916c56' \
                      '28def48bb4129b4099101cf4e6c7c499'
                
        self.name = 'lastpass-cli'
        self.version = '1.2.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['asciidoc', 'cmake',
                        'curl', 'libxml2', 'libxslt', 'openssl', 'pinentry']
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
