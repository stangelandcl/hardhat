from .base import GnuRecipe


class GdkPixBufRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdkPixBufRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd55e5b383ee219bd0e23bf6ed4427d56' \
                      'a7db5379729a6e3e0a0e0eba9a8d8879'

        self.name = 'gdk-pixbuf'
        self.depends = ['shared-mime-info']  # to read image files
        # alternatively configure with --disable-gio-sniffing
        # See https://trac.macports.org/ticket/45354 for how gdk detects
        # image file formats
        self.version = '2.34.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/' \
                   '%s/gdk-pixbuf-$version.tar.xz' % short_version

        self.configure_strip_cross_compile()
        self.configure_args += ['--with-x11',
                                '--host=%s' % self.target_triplet,
                                '--build=%s' % self.target_triplet]
