from .base import GnuRecipe


class LibSecretRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSecretRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9ce7bd8dd5831f2786c935d82638ac42' \
                      '8fa085057cc6780aba0e39375887ccb3'
        self.name = 'libsecret'
        self.version = '0.18.5'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.depends = ['gcrypt', 'glib', 'gobject-introspection', 'vala']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/libsecret/' \
                   '$short_version/libsecret-$version.tar.xz'
        self.configure_args += ['--enable-vala=no']
