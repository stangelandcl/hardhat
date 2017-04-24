from ..base import GnuRecipe


class ModuleBuildRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ModuleBuildRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e74b45d9a74736472b74830599cec0d1' \
                      '123f992760f9cd97104f94bee800b160'

        self.name = 'perl5-module-build'
        self.version = '0.4222'
        self.url = 'http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/' \
                   'Module-Build-$version.tar.gz'

        self.configure_args = ['perl', 'Makefile.PL']
