from .base import SetupPyRecipe
from hardhat.urls import Urls


class PGExtrasRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PGExtrasRecipe, self).__init__(*args, **kwargs)

        self.name = 'pgextras'
        self.pydepends = ['psycopg2']
        self.version = '1e0ad08a1e8b9e2e6725893f4bc32057db444a66'
        self.url = Urls.github_commit('stangelandcl',
                                      'python-pgextras',
                                      self.version)
        self.sha256 = '03591542ecba522cd48ddcf9bd71d8af' \
                      'fe8839b4e3936fbd2f6eb348e77e0c2b'
