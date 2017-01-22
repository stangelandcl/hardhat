from .base import PipBaseRecipe


class CeleryRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CeleryRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1a359c815837f9dbf193a7dbc6addafa' \
                      '34612c077ff70c66e3b16e14eebd2418'

        self.name = 'celery'
        self.version = '3.1.23'
        self.pydepends = ['billiard', 'kombu']
