from .base import GnuRecipe


class PgCluuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PgCluuRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4bc3963dcc752e02734a1f1738b83bb2' \
                      'a97debb1fcce18e4d3a2b34f969a39cc'

        self.name = 'pgcluu'
        self.version = '2.5'
        self.url = 'https://github.com/darold/pgcluu/archive/v$version.tar.gz'
        self.depends = ['perl', 'sysstat']
        self.configure_args = ['perl Makefile.PL']
