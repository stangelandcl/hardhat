from .base import GnuRecipe


class CairoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '613cb38447b76a93ff7235e17acd55a7' \
                      '8b52ea84a9df128c3f2257f8eaa7b252'

        self.name = 'cairo'
        self.version = '1.14.6'
        self.depends = ['fontconfig', 'glib', 'gtk-doc', 'libpng', 'mesa',
                        'pixman', 'xorg-libs']
        self.url = 'http://cairographics.org/releases/cairo-$version.tar.xz'

        self.configure_args += [
            '--enable-tee',
            '--enable-xlib-xcb',
            '--enable-gl',
            '--enable-gtk-doc']
