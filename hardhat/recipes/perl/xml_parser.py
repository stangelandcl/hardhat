from ..base import GnuRecipe


class XmlParserRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XmlParserRecipe, self).__init__(*args, **kwargs)
        self.name = 'perl5-xml-parser'
        self.version = '2.44'
        self.url = 'http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/' \
                   'XML-Parser-$version.tar.gz'

        self.configure_args = ['perl', 'Makefile.PL']
        self.sha256 = '1ae9d07ee9c35326b3d9aad56eae71a' \
                      '6730a73a116b9fe9e8a4758b7cc033216'
