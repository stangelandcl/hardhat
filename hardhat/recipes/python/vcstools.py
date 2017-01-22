from .base import PipBaseRecipe


class VcsToolsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(VcsToolsRecipe, self).__init__(*args, **kwargs)

        self.name = 'vcstools'
        self.version = '0.1.39'
        self.pydepends = ['pyyaml', 'dateutil']
        self.sha256 = '841bdfeca326b532ced45feea2a79b48' \
                      '008415ef117df008071ba74e985f59c1'
