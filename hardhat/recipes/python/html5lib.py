from .base import PipBaseRecipe


class Html5LibRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Html5LibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e793bb51f74c07cf15f4de2fb4fdf0d' \
                      'cc191d644a20d18bd90d82c3c2bccf35'

        self.name = 'html5lib'
        self.version = '0.99999999' # bleach requires this version
        self.pydepends = ['setuptools', 'webencodings']
