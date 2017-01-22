from .base import GnuRecipe


class TinySchemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TinySchemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'eac0103494c755192b9e8f10454d9f98' \
                      'f2bbd4d352e046f7b253439a3f991999'

        self.name = 'tinyscheme'
        self.version = '1.41'
        self.url = 'http://downloads.sourceforge.net/project/$name/$name/' \
                   '$name-$version/$name-$version.tar.gz'

        self.compile_args += ['CC="$CC $CFLAGS -fPIC"']

    def configure(self):
        pass

    def install(self):
        pass
