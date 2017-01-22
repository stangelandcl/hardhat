from .base import SetupPyRecipe


class PyXdgRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyXdgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '81e883e0b9517d624e8b0499eb267b82' \
                      'a815c0b7146d5269f364988ae031279d'
        self.name = 'pyxdg'
        self.version = '0.25'
        self.url = 'http://people.freedesktop.org/~takluyver/' \
                   'pyxdg-$version.tar.gz'

    def compile(self):
        pass

    def install(self):
        self.install_args = [self.python,
                             'setup.py',
                             'install',
                             '--optimize=1',
                             '--force']
        super(SetupPyRecipe, self).install()
