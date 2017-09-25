from .base import GnuRecipe


class MsmtpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MsmtpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'da15db1f62bd0201fce5310adb89c861' \
                      '88be91cd745b7cb3b62b81a501e7fb5e'
        self.name = 'msmtp'
        self.version = '1.6.6'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://downloads.sourceforge.net/msmtp/files/' \
                   '$name-$version.tar.xz'
