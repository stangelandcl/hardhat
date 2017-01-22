from .base import PipBaseRecipe


class NbConvertRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(NbConvertRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b5ed2c356692e8675ad5078c674d8a17' \
                      '7a2eaa1cd662c14dc0b4fb7f0fa64e5c'

        self.name = 'nbconvert'
        self.version = '5.0.0'
        self.pydepends = ['bleach', 'entrypoints', 'mistune', 'pandocfilters',
                          'testpath']
