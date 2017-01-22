from .base import GnuRecipe


class Extra:
    pass


class PopplerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PopplerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '420abaab63caed9e1ee28964a0ba216d' \
                      '1979506726164bc99ad5ade289192a1b'

        self.name = 'poppler'
        self.version = '0.41.0'
        self.depends = ['cairo',
                        'curl',
                        'fontconfig',
                        'gtk2',
                        'libjpeg-turbo',
                        'libpng',
                        'libtiff',
                        'qt5',
                        'pkgconfig']
        self.url = 'http://poppler.freedesktop.org/poppler-$version.tar.xz'
        e = Extra()
        e.name = 'poppler-data'
        e.version = '0.4.7'
        e.url = 'http://poppler.freedesktop.org/' \
                'poppler-data-%s.tar.gz' % e.version
        e.sha256 = 'e752b0d88a7aba54574152143e7bf764' \
                   '36a7ef51977c55d6bd9a48dccde3a7de'
        self.extra_downloads = [e]
        self.configure_args += [
            '--disable-static',
            '--enable-cmyk',
            '--enable-build-type=release',
            '--enable-xpdf-headers',
            '--with-testdatadir=$PWD/testfiles'
            ]

    def extract(self):
        super(PopplerRecipe, self).extract()
        for e in self.extra_downloads:
            self.extract_into(e.filename, self.extract_dir)
