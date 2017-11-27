from ..base import GnuRecipe, SourceMixin

class RPackageBase(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RPackageBase, self).__init__(*args, **kwargs)
        self.install_args = ['R', 'CMD', 'INSTALL', '.']

    def configure(self):
        pass

    def compile(self):
        pass
