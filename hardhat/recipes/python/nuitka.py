from .base import SetupPyRecipe


class NuitkaRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(NuitkaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '29b16b2bdd6894536037b246beb4d04c' \
                      '10c645a7750795fa3bb3b1d2ad110e61'

        self.pythons = ['python2']
        self.name = 'nuitka'
        self.version = '0.5.21'
        self.url = 'http://nuitka.net/releases/Nuitka-$version.tar.bz2'
