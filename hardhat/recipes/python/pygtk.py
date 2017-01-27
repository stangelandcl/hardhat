from .base import PythonGnuRecipe


class PyGtkRecipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyGtkRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python2']
        self.name = 'pygtk'
        self.depends = ['gtk3']
        self.pydepends = ['pygobject2']
        self.version = '2.24.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.sha256 = 'cd1c1ea265bd63ff669e92a2d3c2a88e' \
                      'b26bcd9e5363e0f82c896e649f206912'

        self.url = 'http://ftp.gnome.org/pub/GNOME/sources/pygtk/' \
                   '%s/pygtk-$version.tar.bz2' % short_version
