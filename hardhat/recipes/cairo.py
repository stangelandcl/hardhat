from .base import GnuRecipe


class CairoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairoRecipe, self).__init__(*args, **kwargs)

        self.name = 'cairo'
        self.version = '1.14.8'
        self.depends = ['fontconfig', 'glib', 'gtk-doc', 'libpng', 'mesa',
                        'pixman', 'xorg-libs']
        self.url = 'http://cairographics.org/releases/cairo-$version.tar.xz'

        self.configure_args += [
            '--enable-tee',
            '--enable-xlib-xcb',
            '--enable-gl',
            '--enable-gtk-doc']
