import os
from .base import GnuRecipe


class I3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(I3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '217d524d1fbc85ae346b25f6848d1b7b' \
                      'cd2c23184ec88d29114bf5a621385326'

        self.name = 'i3'
        self.version = '4.15'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://i3wm.org/downloads/'
        self.depends = ['autotools', 'libev', 'startup-notification',
                        'xcb-util-cursor',
                        'xcb-util-keysyms',
                        'xcb-util-renderutil',
                        'xcb-util-xrm',
                        'yajl']
        self.url = 'https://i3wm.org/downloads/i3-$version.tar.bz2'

    def compile(self):
        self.directory = os.path.join(self.directory, self.target_triplet)
        super(I3Recipe, self).compile()

    def install(self):
        super(I3Recipe, self).install()
        self.directory = os.path.dirname(self.directory)

