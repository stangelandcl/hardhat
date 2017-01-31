from ..base import GnuRecipe


class XmlSimpleRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XmlSimpleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b9450ef22ea9644ae5d6ada086dc4300' \
                      'fa105be050a2030ebd4efd28c198eb49'        
        self.name = 'perl5-xml-simple'
        self.version = '2.22'
        self.url = 'http://cpan.org/authors/id/G/GR/GRANTM/XML-Simple-$version.tar.gz'
        self.configure_args = ['perl', 'Makefile.PL']
