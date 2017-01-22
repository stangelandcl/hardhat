from .base import GnuRecipe


class X264Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(X264Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '1a985db59a64fda7dabac73b705ee7b0' \
                      'efac7ab34767a20c4730973b785d299d'

        self.name = 'x264'
        self.version = '20160827-2245'
        self.depends = ['yasm']
        self.url = 'http://download.videolan.org/pub/videolan/x264' \
                   '/snapshots/x264-snapshot-$version-stable.tar.bz2'
        self.configure_args += ['--disable-cli',
                                '--enable-shared']
        self.configure_strip_cross_compile()
        self.environment['AS'] = 'yasm'
