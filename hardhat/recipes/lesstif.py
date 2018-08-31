from .base import GnuRecipe


class LessTiffRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LessTiffRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e5ef90ff30897448a7c090c2e31ceb30' \
                      '2ed064a60411436e8995580848ed1a63'
        self.name = 'lesstiff'
        self.version = '0.95.0'
        self.depends = ['x11']
        self.url = 'http://downloads.sourceforge.net/lesstif/' \
                   'lesstif-$version.tar.bz2'
        self.configure_args += ['--disable-debug',
                                '--enable-production',
                                '--with-xdnd']
