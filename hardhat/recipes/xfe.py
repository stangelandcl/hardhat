from .base import GnuRecipe


class XfeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XfeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a1e3e892584988c80b3a492f7b3cb78e' \
                      '1ee84d7148e6d1fc9d6054bbd8063bec'
        self.description = 'Fast lightweight file manager'
        self.name = 'xfe'
        self.version = '1.42'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'fox']
        self.url = 'http://downloads.sourceforge.net/xfe/' \
                   'xfe-$version.tar.gz'
        self.configure_args += ['--with-x']
        # Fix rpl_malloc undefined when cross-compiling.
        # See http://rickfoosusa.blogspot.com/2011/11/
        # howto-fix-undefined-reference-to.html
        self.configure_strip_cross_compile()
#        self.CFLAGS = self.CXXFLAGS = ' -O0 -ggdb3'
