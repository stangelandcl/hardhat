from .base import GnuRecipe


class UtilLinuxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(UtilLinuxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2c59ea67cc7b564104f60532f6e0a95f' \
                      'e17a91acb870ba8fd7e986f273abf9e7'

        self.description = 'includes uuidgen'
        self.name = 'util-linux'
        self.version = '2.29'
        self.version_regex = 'v(?P<version>\d+\.\d+)/'
        self.version_url = 'https://www.kernel.org/pub/linux/utils/util-linux/'
        self.url = 'https://www.kernel.org/pub/linux/utils/util-linux/' \
                   'v$version/util-linux-$version.tar.xz'

        self.configure_args += ['--disable-chfn-chsh',
                                '--disable-login',
                                '--disable-nologin',
                                '--disable-su',
                                '--disable-setpriv',
                                '--disable-runuser',
                                '--disable-pylibmount',
                                '--without-python',
                                '--without-systemd',
                                '--without-systemdsystemunitdir',
                                '--disable-makeinstall-setuid',
                                '--disable-makeinstall-chown',
                                ]
        self.environment['LDFLAGS'] += ' -lrt'
