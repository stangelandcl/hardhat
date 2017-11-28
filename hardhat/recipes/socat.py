from .base import GnuRecipe


class SocatRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SocatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ce3efc17e3e544876ebce7cd6c85b3c2' \
                      '79fda057b2857fcaaf67b9ab8bdaf034'

        self.name = 'socat'
        self.version = '1.7.3.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'openssl']
        self.url = 'http://www.dest-unreach.org/socat/download/' \
                   'socat-$version.tar.gz'
