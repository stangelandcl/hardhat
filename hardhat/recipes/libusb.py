from .base import GnuRecipe


class LibUsbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUsbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7dce9cce9a81194b7065ee912bcd55ee' \
                      'ffebab694ea403ffb91b67db66b1824b'

        self.name = 'libusb'
        self.version = '1.0.21'
        self.depends = ['doxygen']
        self.url = 'https://github.com//libusb/libusb/releases/download/' \
                   'v$version/libusb-$version.tar.bz2'
