from .base import PythonGnuRecipe


class PyGObjectRecipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyGObjectRecipe, self).__init__(*args, **kwargs)

        self.depends = ['glib', 'gobject-introspection', 'gtk3']
        self.pydepends = ['pycairo']
        self.name = 'pygobject'
        # versions with an odd minor version number (second number) are
        # developmental versions and may show deprecation warnings
        # for instance in 'ipython --pylab'
        self.version = '3.20.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.sha256 = '3d261005d6fed6a92ac4c25f28379255' \
                      '2f7dad865d1b7e0c03c2b84c04dbd745'

        self.url = 'http://ftp.gnome.org/pub/GNOME/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version

    def configure(self):
        self.configure_args += ['--with-python=%s' % self.python]
        super(PyGObjectRecipe, self).configure()
