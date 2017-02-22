import os
from .base import GnuRecipe


class CupsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CupsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f589bb7d5d1dc3aa0915d7cf2b808571' \
                      'ef2e1530cd1a6ebe76ae8f9f4994e4f6'

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
        self.configure_args += ['--with-rcdir=no',
                                '--with-xinetd=no',
                                '--disable-pam',
                                '--disable-dbus',
                                '--disable-systemd',
                                '--with-menudir=no',
                                '--with-icondir=%s/share/icons'
                                % self.prefix_dir,
                                '--with-cups-group=%s' % os.environ['USER']]
        self.install_args += ['CHGRPPROG=/bin/true',
                              'CHOWNPROG=/bin/true',

                              # otherwise mv hangs waiting for user input
                              # asking about changing file mode
                              'MV="mv -f"'
                              ]
