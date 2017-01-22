from .base import SetupPyRecipe


class MeldRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MeldRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '93c4f928319dae7484135ab292fe6ea4' \
                      '254123e8219549a66d3e2deba6a38e67'

        self.pythons = ['python2']
        self.python = 'python2'
        self.name = 'meld'
        self.depends = ['dconf', 'glib', 'gtk3', 'gtksourceview']
        self.pydepends = ['pycairo', 'pygobject']
        self.version = '3.16.4'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'https://download.gnome.org/sources/meld/%s/' \
                   'meld-$version.tar.xz' % short_version

    @property
    def provides(self):
        return ['meld']
