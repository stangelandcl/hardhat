from .base import GnuRecipe


class ClutterRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ClutterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None

        self.name = 'clutter'
        self.version = '1.26.0'
        self.depends = ['atk', 'cogl', 'gtk-doc', 'json-glib']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'ftp://ftp.gnome.org/pub/gnome/sources/$name/%s/' \
                   '$name-$version.tar.xz' % short_version

        self.configure_args += ['--enable-egl-backend',
                                '--enable-gtk-doc']
