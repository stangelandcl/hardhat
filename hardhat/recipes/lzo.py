from .base import GnuRecipe


class LzoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LzoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f294a7ced313063c057c504257f437c8' \
                      '335c41bfeed23531ee4e6a2b87bcb34c'
                      
        self.name = 'lzo'
        self.version = '2.09'
        self.url = 'http://www.oberhumer.com/opensource/lzo/' \
                   'download/lzo-$version.tar.gz'
