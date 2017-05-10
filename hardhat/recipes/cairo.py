from .base import GnuRecipe


class CairoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CairoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd1f2d98ae9a4111564f6de4e013d639c' \
                      'f77155baf2556582295a0f00a9bc5e20'
        
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
