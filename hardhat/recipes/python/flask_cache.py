from .base import PipBaseRecipe


class FlaskCacheRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskCacheRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '90126ca9bc063854ef8ee276e95d38b2' \
                      'b4ec8e45fd77d5751d37971ee27c7ef4'
        self.name = 'flask-cache'
        self.version = '0.13.1'
        self.pydepends = ['flask']
