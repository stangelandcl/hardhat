from .base import PipBaseRecipe


class PyZmqRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyZmqRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0322543fff5ab6f87d11a8a099c4c07d' \
                      'd8a1719040084b6ce9162bcdf5c45c9d'

        self.name = 'pyzmq'
        self.depends = ['zeromq']
        self.version = '16.0.2'
