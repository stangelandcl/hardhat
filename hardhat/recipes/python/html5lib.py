from .base import PipBaseRecipe


class Html5LibRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Html5LibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2612a191a8d5842bfa057e41ba50bbb9' \
                      'dcb722419d2408c78cff4758d0754868'

        self.name = 'html5lib'
        self.version = '0.9999999' # bleach requires this version
        self.pydepends = ['webencodings']
