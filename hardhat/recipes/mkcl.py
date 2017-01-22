from .base import GnuRecipe


class MKCLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MKCLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cefe4da030e1af7aa0ff734c4124b76a' \
                      '4433397cebe398852d4ed94ad9d63d71'

        self.description = 'Common Lisp implementation'
        self.name = 'mkcl'
        self.version = '1.1.9'
        self.url = 'http://common-lisp.net/project/mkcl/releases/' \
                   'mkcl-$version.tar.gz'
        self.configure_strip_cross_compile()
