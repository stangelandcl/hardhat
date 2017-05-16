from .base import PipBaseRecipe


class DefusedXmlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DefusedXmlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '24d7f2f94f7f3cb6061acb215685e512' \
                      '5fbcdc40a857eff9de22518820b0a4f4'

        self.name = 'defusedxml'
        self.version = '0.5.0'
