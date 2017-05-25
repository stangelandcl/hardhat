from .base import GnuRecipe


class GLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f00e5d9e2a2948b1da25fcba734a6b7a' \
                      '40f556de8bc9f528a53f6569969ac5d0'
                
        self.name = 'glib'
        self.version = '2.52.2'
        self.version_regex = '(?P<version>\d+\.\d+)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/glib/'
        self.depends = ['gtk-doc', 'libffi', 'pcre', 'python3', 'util-linux']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % self.short_version

        self.configure_args += ['glib_cv_stack_grows=no',
                                'glib_cv_uscore=false',
                                '--with-pcre=system',
                                '--enable-gtk-doc']
