import os
from .base import GnuRecipe
from ..util import patch


class LinuxPamRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinuxPamRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '241aed1ef522f66ed672719ecf2205ec' \
                      '513fd0075ed80cda8e086a5b1a01d1bb'
        self.name = 'linux-pam'
        self.version = '1.3.0'
        self.depends = ['bdb', 'cracklib', 'libtirpc']
        self.url = 'http://linux-pam.org/library/Linux-PAM-$version.tar.bz2'
        self.sudo = True
        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--disable-regenerate-docu',
            '--enable-securedir=%s/lib/security' % self.prefix_dir,
            '--includedir=%s/include/security' % self.prefix_dir
            ]
        
    def patch(self):
        self.log_dir('patch', self.directory, 'patching config directories')
        src = '"/etc/pam.d'
        dst = '"%s/etc/pam.d' % self.prefix_dir
        filename = os.path.join(self.directory, 'libpam', 'pam_private.h')
        patch(filename, src, dst)
        src = '"/usr/lib/'
        dst = '"%s/lib/' % self.prefix_dir
        patch(filename, src, dst)        

    def install(self):
        super(LinuxPamRecipe, self).install()
        # These files are from BLFS
        self.log_dir('install', self.directory, 'adding etc/pam.d files')
        dir = os.path.join(self.prefix_dir, 'etc', 'pam.d')
        if not os.path.exists(dir):
            os.makedirs(dir)
        def write(filename, text):
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

        # from fedora
        postlogin = r'''#%PAM-1.0
# This file is auto-generated.
# User changes will be destroyed the next time authconfig is run.

session     [success=1 default=ignore] pam_succeed_if.so service !~ gdm* service !~ su* quiet
session     [default=1]   pam_lastlog.so nowtmp showfailed
session     optional      pam_lastlog.so silent noupdate showfailed
'''
        write('postlogin', postlogin)
        
        password_auth = r'''#%PAM-1.0
# This file is auto-generated.
# User changes will be destroyed the next time authconfig is run.
auth        required      pam_env.so
auth        sufficient    pam_unix.so try_first_pass nullok
auth        required      pam_deny.so

account     required      pam_unix.so

password    requisite     pam_pwquality.so try_first_pass local_users_only retry=3 authtok_type=
password    sufficient    pam_unix.so try_first_pass use_authtok nullok sha512 shadow
password    required      pam_deny.so

session     optional      pam_keyinit.so revoke
session     required      pam_limits.so
-session     optional      pam_systemd.so
session     [success=1 default=ignore] pam_succeed_if.so service in crond quiet use_uid
session     required      pam_unix.so
'''
        write('password-auth', password_auth)

        self.log_dir('install', self.directory, 'setuid unix_chkpwd')
        exe = os.path.join(self.prefix_dir, 'sbin', 'unix_chkpwd')
        self.run_sudo(['chown', 'root', exe])
        self.run_sudo(['chmod', '+s', exe])
