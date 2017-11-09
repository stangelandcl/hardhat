from ..base import GnuRecipe, SourceMixin


class RInsideRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RInsideRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6eb3e95162c89ed15debc2d2070aea1e' \
                      '0a2f2448611c82b664a0cc752a90fa1e'
        self.name = 'r-rinside'
        self.version = '764e2a90a857a47f9a45ee1e1f2c4d51498f7ac6'
        self.url = self.github_commit('eddelbuettel', 'rinside')
        self.configure_strip_cross_compile()


class RInsideSourceRecipe(SourceMixin, RInsideRecipe):
    def __init__(self, *args, **kwargs):
        super(RInsideSourceRecipe, self).__init__(*args, **kwargs)
