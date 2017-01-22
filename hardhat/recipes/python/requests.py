from .base import PipBaseRecipe


class RequestsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RequestsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ed98431a0631e309bb4b63c81d561c16' \
                      '54822cb103de1ac7b47e45c26be7ae34'

        self.name = 'requests'
        self.version = '2.12.4'
