from .base import GnuRecipe


class ZVimesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZVimesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2ab424f898bac040fa940cd7a09e576f' \
                      '5abb6464302b6113318a5bce796fc8d6'

        self.description = 'z notation type checker'
        self.name = 'z-vimes'
        self.depends = ['popt']
        self.version = '0.2.9'
        self.url = 'https://download.sourceforge.net/z-vimes/' \
                   'vimes-$version.tar.gz'
        self.configure_strip_cross_compile()
        self.compile_args = ['make']
        # docs installed to share/doc/vimes
