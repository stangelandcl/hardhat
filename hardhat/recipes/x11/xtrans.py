from .base import X11BaseRecipe


class XTransRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XTransRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'adbd3b36932ce4c062cd10f57d78a156' \
                      'ba98d618bdb6f50664da327502bc8301'

        self.name = 'xtrans'
        self.version = '1.3.5'
