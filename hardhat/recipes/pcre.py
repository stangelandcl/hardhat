from .base import GnuRecipe


class PcreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PcreRecipe, self).__init__(*args, **kwargs)
        self.name = 'pcre'
        self.version = '8.42'
        self.url = 'https://ftp.pcre.org/pub/pcre/pcre-$version.tar.gz'
        self.depends = ['bzip2', 'readline', 'zlib']

        self.configure_args += ['--enable-jit',
                                '--enable-utf8',
                                '--enable-pcre16',
                                '--enable-pcre32',
                                '--enable-pcregrep-libz',
                                '--enable-pcregrep-libbz2',
                                '--enable-pcretest-libreadline',
                                '--enable-unicode-properties']
