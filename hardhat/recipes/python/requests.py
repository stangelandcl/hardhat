from .base import PipBaseRecipe


class RequestsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RequestsRecipe, self).__init__(*args, **kwargs)
        self.name = 'requests'
        self.version = '2.18.4'
