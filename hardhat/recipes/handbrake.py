import os
from .base import GnuRecipe


class HandbrakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HandbrakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fb9230dd121b456f6829d1d25ac8bbf7' \
                      '6e503b51c4efc70f0a7fd2bb8607e2f0'

        self.name = 'handbrake'
        self.version = '0.10.5'
        self.depends = ['dbus-glib', 'gudev', 'libdvdcss', 'libnotify',
                        'make', 'tar', 'wget']
        self.url = 'https://handbrake.fr/' \
                   'rotation.php?file=HandBrake-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.compile_args = ['make', '-j1']
        self.environment_strip_lto()
        self.environment['LD'] = self.environment['CXX']

    def compile(self):
        d = self.directory
        self.directory = os.path.join(d, 'build')

        super(HandbrakeRecipe, self).compile()

#        self.directory = d
