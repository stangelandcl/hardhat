from .base import PipBaseRecipe


class ToxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ToxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c3bdc06fe411d24015e8bbbab9d03dc' \
                      '5243a970154496aac13f9283682435f9'
        self.name = 'tox'
        self.version = '2.7.0'
        self.pydepends = ['pluggy', 'py', 'virtualenv']
