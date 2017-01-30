from .base import GnuRecipe
import os


class Graphite2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Graphite2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec0185b663059553fd46e8c4a4f0dede' \
                      '60a02f13a7a1fefc2ce70332ea814567'

        self.name = 'graphite2'
        self.version = '1.3.9'
        self.depends = ['asciidoc',
                        'cmake',
                        'doxygen',
                        'freetype',
                        'python2']
        self.url = 'https://github.com/silnrsi/graphite/releases/download/' \
                   '$version/graphite2-$version.tgz'
        self.configure_args = ['cmake',
                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
                               '..']

    def patch(self):
        self.directory = os.path.join(self.directory, 'build')
        os.makedirs(self.directory)
