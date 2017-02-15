from .base import GnuRecipe


class NpthRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NpthRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bca81940436aed0734eb8d0ff8b179e0' \
                      '4cc8c087f5625204419f5f45d736a82a'
        self.name = 'npth'
        self.version = '1.3'
        self.depends = ['autotools']
        self.url = 'ftp://ftp.gnupg.org/gcrypt/$name/' \
            '$name-$version.tar.bz2'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
