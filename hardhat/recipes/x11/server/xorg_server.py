import os
from hardhat.recipes.base import GnuRecipe
from hardhat.util import patch


class XOrgServerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XOrgServerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '59c99fe86fe75b8164c6567bfc6e982a' \
                      'ecc2e4a51e6fbac1b842d5d00549e918'

        self.name = 'xorg-server'
        self.version = '1.20.1'
        self.depends = ['libepoxy', 'libunwind', 'nettle', 'openssl', 'pixman',
                        'wayland', 'wayland-protocols',
                        'xkeyboard-config', 'xorg-apps']
        self.url = 'http://ftp.x.org/pub/individual/xserver/' \
                   'xorg-server-$version.tar.bz2'

        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--enable-glamor',
            '--enable-xwayland',
            '--disable-xorg',
            #'--enable-install-setuid',
            '--enable-suid-wrapper',
            #'--with-xkb-output=/var/lib/xkb'
            ]
        self.sudo = True
        self.configure_strip_cross_compile()
        self.environment['CFLAGS'] += ' -Wno-error=array-bounds'

    def install(self):
        self.log_dir('install', self.directory, 'removing old libexec/Xorg')
        file = os.path.join(self.prefix_dir, 'libexec', 'Xorg')
        if os.path.exists(file):
            os.remove(file)

        self.log_dir('install', self.directory, 'removing old libexec/Xorg')
        file = os.path.join(self.prefix_dir, 'libexec', 'Xorg.wrap')
        if os.path.exists(file):
            os.remove(file)

        super(XOrgServerRecipe, self).install()

#        exe = '%s/bin/Xorg' % self.prefix_dir
#        self.log_dir('install', self.directory, 'chown root Xorg')
#        self.run_sudo(['chown', 'root', exe])
#        self.log_dir('install', self.directory, 'setuid Xorg')
#        self.run_sudo(['chmod', '+s', exe])

#        exe = '%s/libexec/Xorg.wrap' % self.prefix_dir
#        self.log_dir('install', self.directory, 'chown root Xorg.wrap')
#        self.run_sudo(['chown', 'root', exe])
#        self.log_dir('install', self.directory, 'setuid Xorg.wrap')
#        self.run_sudo(['chmod', '+s', exe])

#        exe = '%s/libexec/Xorg' % self.prefix_dir
#        self.log_dir('install', self.directory, 'chown root libexec/Xorg')
#        self.run_sudo(['chown', 'root', exe])
#        self.log_dir('install', self.directory, 'setuid libexec/Xorg')
#        self.run_sudo(['chmod', '+s', exe])

    def patch(self):
        self.log_dir('patch', self.directory, 'logging')
        src = 'driver = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);'
        dst = r'fprintf(stderr, "dlopen(%s)\n", filename);' + '\n' + src
        filename = os.path.join(self.directory, 'glx', 'glxdricommon.c')
        patch(filename, src, dst)

        src = 'do {'
        dst = r'fprintf(stderr, "path=%s\n", path);' + '\n' + src
        patch(filename, src, dst)

