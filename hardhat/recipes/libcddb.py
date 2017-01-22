from .base import GnuRecipe


class LibcddbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibcddbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '35ce0ee1741ea38def304ddfe84a9589' \
                      '01413aa829698357f0bee5bb8f0a223b'

        self.name = 'libcddb'
        self.version = '1.3.2'
        self.url = 'http://prdownloads.sourceforge.net/libcddb/' \
                   'libcddb-$version.tar.bz2'

        # Fix rpl_malloc undefined when cross-compiling.
        # See http://rickfoosusa.blogspot.com/2011/11/
        # howto-fix-undefined-reference-to.html
        self.configure_strip_cross_compile()
