from .base import PipBaseRecipe


class PkgInfoRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PkgInfoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bb1a6aeabfc898f5df124e7e00303a5b' \
                      '3ec9a489535f346bfbddb081af93f89e'
                
        self.name = 'pkginfo'
        self.version = '1.4.1'
