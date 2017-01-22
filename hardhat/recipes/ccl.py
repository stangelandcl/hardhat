from .base import GnuRecipe


class CCLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CCLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '08e885e8c2bb6e4abd42b8e8e2b60f25' \
                      '7c6929eb34b8ec87ca1ecf848fac6d70'

        self.description = 'Clozure Common Lisp implementation'
        self.name = 'ccl'
        self.version = '1.11'
        self.url = 'ftp://ftp.clozure.com/pub/release/$version/' \
                   'ccl-$version-linuxx86.tar.gz'
