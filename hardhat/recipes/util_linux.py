import os
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
        self.depends = ['linux-pam', 'readline', 'zlib']

        self.configure_args += ['--disable-chfn-chsh',
                                '--disable-su',
                                '--disable-setpriv',
                                '--disable-runuser',
                                '--disable-pylibmount',
                                '--without-python',
                                '--without-systemd',
                                '--without-systemdsystemunitdir',
                                '--disable-makeinstall-setuid',
                                '--disable-makeinstall-chown',
                                '--with-readline',
                                ]
        self.environment['LDFLAGS'] += ' -lrt'

    def install(self):
        super(UtilLinuxRecipe, self).install()
        # These files are from the fedora package util-linux
        self.log_dir('install', self.directory, 'adding etc/pam.d files')

        def write(filename, text):
            dir = os.path.join(self.prefix_dir, 'etc', 'pam.d')
            with open(os.path.join(dir, filename), 'wt') as f:
                f.write(text)

        login = r'''#%PAM-1.0
auth       substack     system-auth
auth       include      postlogin
account    required     pam_nologin.so
account    include      system-auth
password   include      system-auth
# pam_selinux.so close should be the first session rule
session    required     pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_console.so
# pam_selinux.so open should only be followed by sessions to be executed in the user context
session    required     pam_selinux.so open
session    required     pam_namespace.so
session    optional     pam_keyinit.so force revoke
session    include      system-auth
session    include      postlogin
-session   optional     pam_ck_connector.so
'''
        write('login', login)
        remote = r'''#%PAM-1.0
auth       substack     password-auth
auth       include      postlogin
account    required     pam_nologin.so
account    include      password-auth
password   include      password-auth
# pam_selinux.so close should be the first session rule
session    required     pam_selinux.so close
session    required     pam_loginuid.so
# pam_selinux.so open should only be followed by sessions to be executed in the user context
session    required     pam_selinux.so open
session    required     pam_namespace.so
session    optional     pam_keyinit.so force revoke
session    include      password-auth
session    include      postlogin
'''
        write('remote', remote)
        runuser = r'''#%PAM-1.0
auth		sufficient	pam_rootok.so
session		optional	pam_keyinit.so revoke
session		required	pam_limits.so
session		required	pam_unix.so
'''
        write('runuser', runuser)
        chsh = r'''
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    include      system-auth
'''
        write('chsh-chfn', chsh)
        runuserl = r'''#%PAM-1.0
auth		include		runuser
session		optional	pam_keyinit.so force revoke
-session	optional	pam_systemd.so
session		include		runuser
'''
        write('runuser-l', runuserl)
        sul = r'''#%PAM-1.0
auth		include		su
account		include		su
password	include		su
session		optional	pam_keyinit.so force revoke
session		include		su
'''
        write('sul', sul)
        su = r'''#%PAM-1.0
auth		sufficient	pam_rootok.so
# Uncomment the following line to implicitly trust users in the "wheel" group.
#auth		sufficient	pam_wheel.so trust use_uid
# Uncomment the following line to require a user to be in the "wheel" group.
#auth		required	pam_wheel.so use_uid
auth		substack	system-auth
auth		include		postlogin
account		sufficient	pam_succeed_if.so uid = 0 use_uid quiet
account		include		system-auth
password	include		system-auth
session		include		system-auth
session		include		postlogin
session		optional	pam_xauth.so
'''
        write('su', su)
