from .base import PipBaseRecipe


class WTFormsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WTFormsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ffdf10bd1fa565b8233380cb77a304cd' \
                      '36fd55c73023e91d4b803c96bc11d46f'
        self.name = 'wtforms'
        self.version = '2.1'
