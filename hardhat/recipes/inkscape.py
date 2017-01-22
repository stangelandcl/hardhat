from .base import GnuRecipe


class InkscapeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(InkscapeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4d901f8a9e1924404e797ad23b8b0c49' \
                      '5a9d155448816d95a55974314e1f141b'
        self.name = 'inkscape'
        self.version = '0.91'
        self.version_regex = r'(?P<version>\d+\.\d+)'
        self.version_url = 'https://launchpad.net/inkscape/'
        self.depends = ['boost', 'gc', 'gsl', 'gtkmm', 'libxslt', 'popt']
        self.url = 'https://launchpad.net/inkscape/$version.x/' \
                   '$version/+download/inkscape-$version.tar.bz2'
