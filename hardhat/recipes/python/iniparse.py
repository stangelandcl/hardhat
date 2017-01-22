from .base import PipBaseRecipe


class IniParseRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IniParseRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'abc1ee12d2cfb2506109072d6c21e40b' \
                      '6c75a3fe90a9c924327d80bc0d99c054'

        self.name = 'iniparse'
        self.version = '0.4'
