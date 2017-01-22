from .base import GnuRecipe


class GLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f113b7330f4b4a43e3e401fe7849e751' \
                      '831060d574bd936a63e979887137a74a'

        self.name = 'glib'
        self.version = '2.51.0'
        self.version_regex = '(?P<version>\d+\.\d+)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/glib/'
        self.depends = ['gtk-doc', 'libffi', 'pcre', 'python3', 'util-linux']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % self.short_version

        self.configure_args += ['glib_cv_stack_grows=no',
                                'glib_cv_uscore=false',
                                '--with-pcre=system',
                                '--enable-gtk-doc']
