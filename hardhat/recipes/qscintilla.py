import os
from .base import GnuRecipe


class QScintillaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(QScintillaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f2c8ccdc9d3dbb90764ceed53ea096da' \
                      '9bb13b6260da1324e6ab4ecea29e620a'

        self.name = 'qscintilla'
        self.depends = ['qt5']
        self.version = '2.9.2'
        self.url = 'http://sourceforge.net/projects/pyqt/files/QScintilla2/' \
                   'QScintilla-$version/QScintilla_gpl-$version.tar.gz'

    def configure(self):
        self.configure_args = ['qmake', 'qscintilla.pro']
        self.directory = os.path.join(self.directory, 'Qt4Qt5')
        super(QScintillaRecipe, self).configure()
