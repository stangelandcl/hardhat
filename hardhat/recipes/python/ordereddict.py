from .base import PipBaseRecipe


class OrderedDictRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(OrderedDictRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1c35b4ac206cef2d24816c89f89cf289' \
                      'dd3d38cf7c449bb3fab7bf6d43f01b1f'
        self.name = 'ordereddict'
        self.version = '1.1'
