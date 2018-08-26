from .base import GnuRecipe


class PcreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PcreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '69acbc2fbdefb955d42a4c606dfde800' \
                      'c2885711d2979e356c0636efde9ec3b5'
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
