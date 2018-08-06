from .base import GnuRecipe


class CairoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8c90f00c500b2299c0a323dd9beead2a' \
                      '00353752b2092ead558139bd67f7bf16'
        self.name = 'cairo'
        self.version = '1.14.12'
        self.depends = ['fontconfig', 'glib', 'gtk-doc', 'libpng', 'mesa',
                        'pixman', 'xorg-libs']
        self.url = 'http://cairographics.org/releases/cairo-$version.tar.xz'

        self.configure_args += [
            '--enable-tee',
            '--enable-xlib-xcb',
            '--enable-gl',
            '--enable-gtk-doc']
