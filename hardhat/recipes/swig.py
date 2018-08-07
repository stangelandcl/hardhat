from .base import GnuRecipe


class SwigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7cf9f447ae7ed1c51722efc45e7f1441' \
                      '8d15d7a1e143ac9f09a668999f4fc94d'
        self.name = 'swig'
        self.depends = ['pcre']
        self.version = '3.0.12'
        self.version_url = 'http://www.swig.org/download.html'
        self.url = 'http://prdownloads.sourceforge.net/swig/' \
                   'swig-$version.tar.gz'
