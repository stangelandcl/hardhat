from .base import GnuRecipe


class Pcre2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Pcre2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e07d538704aa65e477b6a392b32ff9fc' \
                      '5edf75ab9a40ddfc876186c4ff4d68ac'

        self.name = 'pcre2'
        self.version = '10.31'
        self.url = 'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/' \
                   'pcre2-$version.tar.bz2'
        self.depends = ['bzip2', 'readline', 'zlib']

        self.configure_args += ['--enable-jit',
                                '--enable-utf8',
                                '--enable-unicode',
                                '--enable-pcre2-16',
                                '--enable-pcre2-32',
                                '--enable-pcre2grep-libz',
                                '--enable-pcre2grep-libbz2',
                                '--enable-pcre2test-libreadline',
                                '--enable-unicode-properties']
