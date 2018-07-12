from .base import SetupPyRecipe


class MeldRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MeldRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python3']
        self.python = 'python3'
        self.name = 'meld'
        self.depends = ['dconf', 'glib', 'gtk3', 'gtksourceview',
                        'itstool']
        self.pydepends = ['pycairo', 'pygobject']
        self.version = '3.18.2'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'https://download.gnome.org/sources/meld/%s/' \
                   'meld-$version.tar.xz' % short_version

    @property
    def provides(self):
        return ['meld']
