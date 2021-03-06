from .base import GnuRecipe


class GdkPixBufRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdkPixBufRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fff85cf48223ab60e3c3c8318e208713' \
                      '1b590fd6f1737e42cb3759a3b427a334'
        self.name = 'gdk-pixbuf'
        self.depends = ['shared-mime-info']  # to read image files
        # alternatively configure with --disable-gio-sniffing
        # See https://trac.macports.org/ticket/45354 for how gdk detects
        # image file formats
        self.version = '2.36.12'
        self.version_regex = '(?P<version>\d+\.\d+)'
        self.version_url = 'http://ftp.acc.umu.se/pub/GNOME/sources/gdk-pixbuf/'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/' \
                   '%s/gdk-pixbuf-$version.tar.xz' % short_version

        self.configure_strip_cross_compile()
        self.configure_args += ['--with-x11',
                                '--host=%s' % self.target_triplet,
                                '--build=%s' % self.target_triplet]
