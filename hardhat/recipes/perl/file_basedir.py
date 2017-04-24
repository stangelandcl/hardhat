from ..base import GnuRecipe


class FileBaseDirRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FileBaseDirRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '120a57ef78535e13e1465717b4056aff' \
                      '4ce69af1e31c67c65d1177a52169082b'

        self.name = 'perl5-file-basedir'
        self.depends = ['perl5-module-build']
        self.version = '0.07'
        self.url = 'http://search.cpan.org/CPAN/authors/id/K/KI/KIMRYAN/' \
                   'File-BaseDir-$version.tar.gz'

        self.configure_args = ['perl', 'Makefile.PL']
