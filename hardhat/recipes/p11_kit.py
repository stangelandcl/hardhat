from .base import GnuRecipe


class P11KitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(P11KitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ba726ea8303c97467a33fca50ee79b7b' \
                      '35212964be808ecf9b145e9042fdfaf0'

        self.name = 'p11-kit'
        self.version = '0.23.2'
        self.url = 'https://p11-glue.freedesktop.org/releases/' \
            'p11-kit-%s.tar.gz' % (self.version)
