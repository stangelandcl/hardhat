from .base import GnuRecipe


class ExpectRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ExpectRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b28dca90428a3b30e650525cdc16255d' \
                      '76bb6ccd65d448be53e620d95d5cc040'

        self.name = 'expect'
        self.version = '5.45'
        self.depends = ['tcl']  # tk is optional (for GUI)
        self.url = 'http://prdownloads.sourceforge.net/expect/' \
                   'expect$version.tar.gz'

        self.configure_args += ['--enable-shared']
        self.configure_strip_cross_compile()
