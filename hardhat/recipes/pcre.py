from .base import GnuRecipe


class PcreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PcreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9883e419c336c63b0cb5202b09537c14' \
                      '0966d585e4d0da66147dc513da13e629'
        self.name = 'pcre'
        self.version = '8.38'
        self.url = 'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/' \
                   'pcre-$version.tar.gz'
        self.depends = ['bzip2', 'readline', 'zlib']

        self.configure_args += ['--enable-jit',
                                '--enable-utf8',
                                '--enable-pcre16',
                                '--enable-pcre32',
                                '--enable-pcregrep-libz',
                                '--enable-pcregrep-libbz2',
                                '--enable-pcretest-libreadline',
                                '--enable-unicode-properties']
