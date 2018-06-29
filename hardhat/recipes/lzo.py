from .base import GnuRecipe


class LzoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LzoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c0f892943208266f9b6543b3ae308fab' \
                      '6284c5c90e627931446fb49b4221a072'

        self.name = 'lzo'
        self.version = '2.10'
        self.url = 'http://www.oberhumer.com/opensource/lzo/' \
                   'download/lzo-$version.tar.gz'
        # build with -fPIC because cairo tries to use the
        # static lzo library to make a dynamic library
        self.configure_args += ['--with-pic']
