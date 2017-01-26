from .base import GnuRecipe


class LibInputRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibInputRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '91206c523b4e7aeecf296d0b94276c61' \
                      'bea90b9260d198c8ee3a91eced10a6e3'

        self.name = 'libinput'
        self.version = '1.5.3'
        self.depends = ['check', 'doxygen', 'dot', 'gtk3',
                        'libevdev', 'mtdev']
        # libwacom - not working yet
        self.url = 'http://www.freedesktop.org/software/libinput/' \
                   'libinput-$version.tar.xz'
        self.configure_args += ['--disable-libwacom']
