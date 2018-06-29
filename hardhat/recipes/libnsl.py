from .base import GnuRecipe


class LibNslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibNslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a5a28ef17c4ca23a005a729257c95962' \
                      '0b09f8c7f99d0edbfe2eb6b06bafd3f8'

        self.name = 'libnsl'
        self.version = '1.2.0'
        self.version_regex = r'(v?|libnsl-)(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.version_url = 'https://github.com/thkukuk/libnsl/releases'
        self.url = 'https://github.com/thkukuk/libnsl/archive/' \
                   'v$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
