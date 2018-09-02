from .base import GnuRecipe


class ScDocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ScDocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2bc96daae0ddfb858305e550eb00a544' \
                      'a7a6255edd0bd169dcb2fc0c035eca92'
        self.name = 'scdoc'
        self.version = '1.4.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://git.sr.ht/~sircmpwn/scdoc'
        self.url = 'https://git.sr.ht/~sircmpwn/scdoc/snapshot/scdoc-$version.tar.xz'
