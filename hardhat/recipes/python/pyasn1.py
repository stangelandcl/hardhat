from .base import PipBaseRecipe


class PyAsn1Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyAsn1Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '738c4ebd88a718e700ee35c8d129acce' \
                      '2286542daa80a82823a7073644f706ad'

        self.name = 'pyasn1'
        self.version = '0.2.3'
