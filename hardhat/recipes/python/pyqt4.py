from .base import PythonBaseRecipe
from ..base import GnuRecipe


class PyQt4Recipe(PythonBaseRecipe, GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyQt4Recipe, self).__init__(*args, **kwargs)

        self.depends = ['qt5']
        self.pydepends = ['sip']
        self.name = 'pyqt4'
        self.version = '4.11.4'
        self.sha256 = 'fc1fe77495432ba3b0d74ff5cb164d37' \
                      '5a97f5dddb728256330f615a7cdcf407'
        self.url = 'http://sourceforge.net/projects/pyqt/files/PyQt4/' \
                   'PyQt-$version/PyQt-x11-gpl-$version.tar.gz'

    def configure(self):
        self.configure_args = [self.python,
                               'configure.py',
                               '--confirm-license',
                               '--bindir=%s/bin' % self.prefix_dir]
        super(PyQt4Recipe, self).configure()
