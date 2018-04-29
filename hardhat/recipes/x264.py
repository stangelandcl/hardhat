from .base import GnuRecipe


class X264Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(X264Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ed735c6a5fa6a1f308ea3ec1aa30f2a8' \
                      '4e1a6a81784642e967bb07938ddf3e81'

        self.name = 'x264'
        self.version = '20180429-2245'
        self.depends = ['nasm']
        self.url = 'http://download.videolan.org/pub/videolan/x264' \
                   '/snapshots/x264-snapshot-$version-stable.tar.bz2'
        self.configure_args += ['--disable-cli',
                                '--enable-shared']
        self.configure_strip_cross_compile()
        self.environment['AS'] = 'nasm'
