from .base import PipBaseRecipe


class AutomatRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AutomatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c1fd04ecf08ac87b4dd3feae409542e' \
                      '9bf7827257097b2b6ed5692f69d6f6a8'

        self.pythons = ['python3']
        self.pydepends = ['attrs', 'six']
        self.name = 'Automat'
        self.version = '0.6.0'
