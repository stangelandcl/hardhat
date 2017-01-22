from .base import GnuRecipe


class LibXsltRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXsltRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5fc7151a57b89c03d7b825df5a0fae0a' \
                      '8d5f05674c0e7cf2937ecec4d54a028c'

        self.name = 'libxslt'
        self.version = '1.1.28'
        self.depends = ['gcrypt', 'libxml2', 'python2']
        self.url = 'ftp://xmlsoft.org/libxslt/libxslt-$version.tar.gz'
