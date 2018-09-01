from .base import GnuRecipe


class NetsurfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NetsurfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'eb4864d4459d6f9958dd10a3301c272e' \
                      'a7f5df72667a7db0aad5bc5ae06c0e10'
        self.name = 'netsurf'
        self.version = '3.8'
        self.version_regex = r'netsurf\-(?P<version>\d+\.\d+\.\d+)\-src'
        self.version_url = 'http://www.netsurf-browser.org/downloads/gtk/'
        self.depends = ['autotools', 'cairo', 'gtk2', 'libpng', 'openssl',
                        'pango' 'zlib']
        self.url = 'http://download.netsurf-browser.org/netsurf/releases/' \
                   'source-full/netsurf-all-$version.tar.gz'
