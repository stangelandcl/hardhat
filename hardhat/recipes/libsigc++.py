from .base import GnuRecipe


class LibSigCppRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSigCppRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '774980d027c52947cb9ee4fac6ffe2ca' \
                      '60cc2f753068a89dfd281c83dbff9651'

        self.name = 'libsigc++'
        self.version = '2.8.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version
