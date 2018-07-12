from .base import PipBaseRecipe


class HyperlinkRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HyperlinkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f01b4ff744f14bc5d0a22a6b9f1525ab' \
                      '7d6312cb0ff967f59414bbac52f0a306'
        self.pydepends = ['idna']
        self.name = 'hyperlink'
        self.version = '18.0.0'
