from .base import GnuRecipe
from .util_linux import UtilLinuxRecipe


class LoginRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LoginRecipe, self).__init__(*args, **kwargs)

        util = UtilLinuxRecipe(settings=self)
        self.sha256 = util.sha256
        self.description = 'provides PAM login'
        self.name = 'login'
        self.version = util.version
        self.version_regex = util.version_regex
        self.version_url = util.version_url
        self.url = util.url
        self.depends = ['linux-pam']
        self.configure_args += ['--disable-chfn-chsh',
                                '--enable-login',
                                '--enable-nologin',
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
