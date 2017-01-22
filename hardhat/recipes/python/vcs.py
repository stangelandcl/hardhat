from .base import PipBaseRecipe


class VcsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(VcsRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python2']
        self.name = 'vcs'
        self.version = '0.4.0'
        self.sha256 = '5e2e84d1448bd969a383796c62719952' \
                      '348cc9742f818f1bc95e94faf3d45451'
