from .base import GnuRecipe


class SconsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SconsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'eb296b47f23c20aec7d87d35cfa386d3' \
                      '508e01d1caa3040ea6f5bbab2292ace9'

        self.name = 'scons'
        self.version = '2.5.0'
        self.url = 'http://downloads.sourceforge.net/scons/' \
                   'scons-$version.tar.gz'

        self.install_args = ['python',
                             'setup.py',
                             'install',
                             '--prefix=%s' % self.prefix_dir,
                             '--standard-lib',
                             '--optimize=1']

    def configure(self):
        pass

    def compile(self):
        pass
