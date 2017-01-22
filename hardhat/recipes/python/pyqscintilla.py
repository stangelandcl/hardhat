import os
from .base import PythonBaseRecipe
from ..base import GnuRecipe


class PyQscintillaRecipe(PythonBaseRecipe, GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyQscintillaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f2c8ccdc9d3dbb90764ceed53ea096da' \
                      '9bb13b6260da1324e6ab4ecea29e620a'

        self.depends = ['qt5', 'qscintilla']
        self.pydepends = ['pyqt4', 'sip']
        self.name = 'pyqscintilla'
        self.version = '2.9.2'
        self.url = 'http://sourceforge.net/projects/pyqt/files/QScintilla2/' \
                   'QScintilla-$version/QScintilla_gpl-$version.tar.gz'

    def configure(self):
        self.directory = os.path.join(self.directory, 'Python')
        self.configure_args = [self.python,
                               'configure.py']
        super(PyQscintillaRecipe, self).configure()
