from .base import GnuRecipe


class OtterRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OtterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b4dee6cdf9fec46169b973ad8578d32a' \
                      '30805ea9ecdf95851f24920485f6bddb'
        self.name = 'otter'
        self.version = '0.9.99.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/OtterBrowser/otter-browser/releases'
        self.depends = ['autotools', 'hunspell', 'openssl', 'qt5', 'qtwebengine']
        self.url = 'https://github.com/OtterBrowser/otter-browser/archive/' \
                   'v$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-Wno-dev'
            ]
