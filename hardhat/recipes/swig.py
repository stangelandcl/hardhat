from .base import GnuRecipe


class SwigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9031d531d7418829a54d0d51c4ed900' \
                      '7016b213657ec70be44031951810566e'

        self.name = 'swig'
        self.depends = ['pcre']
        self.version = '3.0.11'
        self.version_url = 'http://www.swig.org/download.html'
        self.url = 'http://prdownloads.sourceforge.net/swig/' \
                   'swig-$version.tar.gz'
