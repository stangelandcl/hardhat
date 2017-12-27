from .base import GnuRecipe


class LibreSslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibreSslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '638a20c2f9e99ee283a841cd787ab4d8' \
                      '46d1880e180c4e96904fc327d419d11f'

        self.name = 'libressl'
        self.version = '2.6.4'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'
        self.depends = ['autotools', 'pkgconfig', 'zlib']
        self.url = 'https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/' \
                   'libressl-$version.tar.gz'
