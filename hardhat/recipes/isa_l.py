from .base import GnuRecipe


class IsaLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IsaLRecipe, self).__init__(*args, **kwargs)
        self.doc = 'Intel storage library. fast DEFLATE compression'
        self.sha256 = 'fc209eb6057308b59d5721ea8542ade4' \
                      'be595e7ecb158bb6c0db3184e6d10a5d'
        self.name = 'isa-l'
        self.version = '2.24.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/01org/isa-l/releases'
        self.depends = ['autotools']
        self.url = 'https://github.com/01org/isa-l/archive/v$version.tar.gz'
        self.compile_args = ['make', '-f', 'Makefile.unx']
        self.install_args = ['make', '-f', 'Makefile.unx',
                             'prefix=%s' % self.prefix_dir]

    def configure(self):
        pass
