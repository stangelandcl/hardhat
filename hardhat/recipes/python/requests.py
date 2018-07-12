from .base import PipBaseRecipe


class RequestsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RequestsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec22d826a36ed72a7358ff3fe56cbd4b' \
                      'a69dd7a6718ffd450ff0e9df7a47ce6a'

        self.name = 'requests'
        self.version = '2.19.1'
        self.pydepends = ['certifi', 'chardet', 'idna', 'urllib3']
