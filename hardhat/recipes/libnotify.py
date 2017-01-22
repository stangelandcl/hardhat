from .base import GnuRecipe


class LibNotifyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibNotifyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0ef61ca400d30e28217979bfa0e73a74' \
                      '06b19c32dd76150654ec5b2bdf47d837'

        self.name = 'libnotify'
        self.version = '0.7.6'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['gobject-introspection', 'gtk3', 'gtk-doc']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/libnotify/%s/' \
                   'libnotify-$version.tar.xz' % short_version
        self.configure_args += ['--enable-gtk-doc']
