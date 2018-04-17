from .base import RPackageBase
from ..base import SourceMixin


class GgeRecipe(RPackageBase):
    def __init__(self, *args, **kwargs):
        super(GgeRecipe, self).__init__(*args, **kwargs)
# GGE 1.2
#        self.sha256 = '143d17990687b78a031416cfa714b08f' \
#                      '45653fcd002c942a36e9a0ac3ba97c02'
        self.sha256 = '33c625aebe1e4dc1d65ea5f8db246391' \
                      '0004da8c92407cac28fe64496aa50c2f'
                                
        self.name = 'r-gge'
        self.version = '1.3'
        self.url = 'https://cran.r-project.org/src/contrib/gge_$version.tar.gz'
        self.configure_strip_cross_compile()


class GgeSourceRecipe(SourceMixin, GgeRecipe):
    def __init__(self, *args, **kwargs):
        super(GgeSourceRecipe, self).__init__(*args, **kwargs)
