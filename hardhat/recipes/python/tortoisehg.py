from .base import SetupPyRecipe


class TortoiseHgRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(TortoiseHgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '56ac0eb7734fa77130e5428e0ccaa1df' \
                      '07526e95da4b1cf501909284d2d00caa'

        self.pythons = ['python2']
        self.python = 'python2'
        self.pydepends = ['iniparse', 'libcanberra', 'pygments',
                          'pyqscintilla', 'pyqt4']
        self.name = 'tortoisehg'
        self.version = '4.0.1'
        self.url = 'http://bitbucket.org/tortoisehg/targz/downloads/' \
                   'tortoisehg-$version.tar.gz'

    @property
    def provides(self):
        return ['tortoisehg']
