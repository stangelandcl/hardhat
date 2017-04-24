from .base import GnuRecipe


class LibWebPRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibWebPRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c928119229d4f8f35e20113ffb61f281' \
                      'eda267634a8dc2285af4b0ee27cf2b40'
        self.name = 'libwebp'
        self.version = '0.6.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'http://downloads.webmproject.org/releases/webp/' \
                   'libwebp-$version.tar.gz'
        self.depends = ['giflib', 'libjpeg-turbo', 'libpng', 'libtiff']
        self.configure_args += [
            '--enable-libwebpmux',
            '--enable-libwebpdemux',
            '--enable-libwebpdecoder',
            '--enable-libwebpextras',
            '--enable-swap-16bit-csp'
            ]
