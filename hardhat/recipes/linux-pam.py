import os
from .base import GnuRecipe


class LinuxPamRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinuxPamRecipe, self).__init__(*args, **kwargs)
        self.name = 'linux-pam'
        self.version = '1.3.0'
        self.depends = ['bdb', 'cracklib', 'libtirpc']
        self.url = 'http://linux-pam.org/library/Linux-PAM-$version.tar.bz2'

        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--disable-regenarate-docu',
            '--enable-securedir=%s/lib/security' % self.prefix_dir,
            ]

#    def install(self):
#        super(LinuxPamRecipe, self).install()

#        text = r'''auth     required       pam_deny.so
#account  required       pam_deny.so
#password required       pam_deny.so
#session  required       pam_deny.so
#'''
#        dir = os.path.join(self.prefix_dir, 'etc', 'other')
#        with open(dir, 'wt') as f:
#            f.write(text)