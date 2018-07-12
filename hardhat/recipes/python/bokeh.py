from .base import PipBaseRecipe


class BokehRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BokehRecipe, self).__init__(*args, **kwargs)

        self.name = 'bokeh'
        self.version = '0.13.0'
        self.pydepends = ['pyyaml', 'requests', 'tornado']
