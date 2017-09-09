from .base import SetupPyRecipe


class MeldRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MeldRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0f499a7fed47e557dc49afff140b1dc5' \
                      'eb2ee99ca265c45e923862d2c0d8f1df'
                
        self.pythons = ['python3']
        self.python = 'python3'
        self.name = 'meld'
        self.depends = ['dconf', 'glib', 'gtk3', 'gtksourceview',
                        'itstool']
        self.pydepends = ['pycairo', 'pygobject']
        self.version = '3.17.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'https://download.gnome.org/sources/meld/%s/' \
                   'meld-$version.tar.xz' % short_version

    @property
    def provides(self):
        return ['meld']
