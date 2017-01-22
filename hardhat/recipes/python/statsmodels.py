from .base import PipBaseRecipe


class StatsModelsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(StatsModelsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ae9a016beccd8f1c9d22bb0b5d9ffb2' \
                      '3ff8013125da5b205684a5fc4e14c65c'

        self.name = 'statsmodels'
        self.version = '0.8.0rc1'
        self.pydepends = ['patsy']
