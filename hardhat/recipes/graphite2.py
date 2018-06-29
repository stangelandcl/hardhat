from .base import GnuRecipe
import os


class Graphite2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Graphite2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bab92ed1844d6538e7e5bda76f6ac9aa' \
                      'f633e38b683983b942c78c8ce063ad7c'
        self.name = 'graphite2'
        self.version = '1.3.11'
        self.depends = ['asciidoc',
                        'cmake',
                        'doxygen',
                        'freetype',
                        'python2']
        self.version_url = 'https://github.com/silnrsi/graphite/releases'
        self.url = 'https://github.com/silnrsi/graphite/releases/download/' \
                   '$version/graphite2-$version.tgz'
        self.configure_args = ['cmake',
                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
                               '..']

    def patch(self):
        self.directory = os.path.join(self.directory, 'build')
        os.makedirs(self.directory)
