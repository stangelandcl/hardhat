from .base import PipBaseRecipe


class RequestsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RequestsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c443e7324ba5b85070c4a818ade28bf' \
                      'abedf16ea10206da1132edaa6dda237e'
        self.name = 'requests'
        self.version = '2.18.4'
        self.pydepends = ['certifi', 'chardet', 'idna', 'urllib3']
