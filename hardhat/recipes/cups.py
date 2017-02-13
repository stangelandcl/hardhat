from .base import GnuRecipe


class CupsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CupsRecipe, self).__init__(*args, **kwargs)
        self.description = r'''The Common Unix Printing System (CUPS) is a
print spooler and associated utilities. It is based on the "Internet Printing
Protocol" and provides printing services to most PostScript and raster
printers.'''
        self.name = 'cups'
        self.version = '2.2.2'
        self.version_url = 'https://github.com/apple/cups/releases'
        self.depends = ['colord',
                        'dbus',
                        'gnutls',
                        'libusb']
        self.url = 'https://github.com/apple/cups/releases/download/' \
                   'v$version/cups-$version-source.tar.gz'
