from .base import PipBaseRecipe


class SeabornRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SeabornRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa274344b1ee72f723bab751c40a5c67' \
                      '1801d47a29ee9b5e69fcf63a18ce5c5d'

        self.pydepends = ['matplotlib', 'pandas', 'scipy']
        self.name = 'seaborn'
        self.version = '0.7.1'
