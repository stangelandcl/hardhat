from .base import RPackageBase
from ..base import SourceMixin


class NipalsRecipe(RPackageBase):
    def __init__(self, *args, **kwargs):
        super(NipalsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bae93f8254166ee62ced3ae372c25271' \
                      '3945f5fc51f8303ba574744264ed3241'
        self.name = 'r-nipals'
        self.version = '0.4'
        self.url = 'https://cran.r-project.org/src/contrib/' \
                   'nipals_$version.tar.gz'
        self.configure_strip_cross_compile()


class NipalsSourceRecipe(SourceMixin, NipalsRecipe):
    def __init__(self, *args, **kwargs):
        super(NipalsSourceRecipe, self).__init__(*args, **kwargs)
