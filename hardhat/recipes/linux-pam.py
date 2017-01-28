import os
from .base import GnuRecipe


class LinuxPamRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinuxPamRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '241aed1ef522f66ed672719ecf2205ec' \
                      '513fd0075ed80cda8e086a5b1a01d1bb'
        self.name = 'linux-pam'
        self.version = '1.3.0'
        self.depends = ['bdb', 'cracklib', 'libtirpc']
        self.url = 'http://linux-pam.org/library/Linux-PAM-$version.tar.bz2'

        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--disable-regenerate-docu',
            '--enable-securedir=%s/lib/security' % self.prefix_dir,
            '--includedir=%s/include/security' % self.prefix_dir
            ]

    def install(self):
        super(LinuxPamRecipe, self).install()
        # These files are from the fedora package util-linux
        self.log_dir('install', self.directory, 'adding etc/pam.d files')

        def write(filename, text):
            dir = os.path.join(self.prefix_dir, 'etc', 'pam.d')
            with open(os.path.join(dir, filename), 'wt') as f:
                f.write(text)
        other = r'''
auth            required        pam_unix.so     nullok
account         required        pam_unix.so
session         required        pam_unix.so
password        required        pam_unix.so     nullok
'''
        write('other', other)
        system_account = r'''account   required    pam_unix.so
'''
        write('system-account', system_account)

        system_auth = r'''auth      required    pam_unix.so
'''
        write('system-auth', system_auth)
        system_session = r'''session   required    pam_unix.so
'''
        write('system-session', system_session)
        system_password = r'''# check new passwords for strength (man pam_cracklib)
password  required    pam_cracklib.so   type=Linux retry=3 difok=5 \
                                        difignore=23 minlen=9 dcredit=1 \
                                        ucredit=1 lcredit=1 ocredit=1 \
                                        dictpath=/lib/cracklib/pw_dict
# use sha512 hash for encryption, use shadow, and use the
# authentication token (chosen password) set by pam_cracklib
# above (or any previous modules)
password  required    pam_unix.so       sha512 shadow use_authtok
'''
        write('system-password', system_password)
        other = r'''
auth        required        pam_warn.so
auth        required        pam_deny.so
account     required        pam_warn.so
account     required        pam_deny.so
password    required        pam_warn.so
password    required        pam_deny.so
session     required        pam_warn.so
session     required        pam_deny.so
'''
        write('other', other)
