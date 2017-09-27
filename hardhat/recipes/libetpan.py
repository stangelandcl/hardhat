from .base import GnuRecipe


class LibEtpanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEtpanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4e67a7b4abadcf3cc16fa16e1621a68e' \
                      '54d489dadfd9a7d1f960c172e953b6eb'
        self.name = 'libetpan'
        self.version = '1.8'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'https://github.com/dinhviethoa/libetpan/archive/' \
                   '$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
