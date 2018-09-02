import os
from .base import GnuRecipe
from ..version import extension_regex


class SwayRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwayRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2af2e6091c14657c651ad26e7c17c547' \
                      'aaf5aef26e8dd4a1e3f37bb620084fda'

        self.name = 'sway'
        self.depends = ['cairo', 'dmenu', 'fonts',
                        'gdk-pixbuf',
                        'json-c', 'libcap', 'linux-pam',
                        'meson', 'pango',
                        'pcre', 'pkgconfig', 'scdoc', 'util-linux',
                        'wayland', 'wlc', 'wlroots', 'xf86-video-fbdev',
                        'xorg-server']
        # Plus install a specific driver for better performance
        # see recipes/x11/drivers for a list
        # Also install the synaptics driver in that directory
        # for laptop touchpad support
        self.environment['CFLAGS'] += ' -Wno-error=maybe-uninitialized'
        self.version = 'de9e80459a93598bdaf6a68485215ce597131d88'
        self.version_regex = r'(?P<version>\d+\.\d+(-rc\d+)?)' \
            + extension_regex
        self.version_url = 'https://github.com/SirCmpwn/sway/releases'
        self.url = 'https://github.com/SirCmpwn/sway/archive/$version.tar.gz'
        self.configure_args = ['meson', 'build',
                               '--prefix %s' % self.prefix_dir,
                               '--buildtype', 'release']
        self.compile_args = ['ninja', '-C', 'build']
        self.install_args = ['%s/bin/ninja' % self.prefix_dir,
                             '-C', 'build', 'install']
        self.sudo = True
# to set keyboard layout. run these commands before starting sway
#    export XKB_DEFAULT_LAYOUT=us
#    export XKB_DEFAULT_VARIANT=dvorak

# to run sway with logging 'sway -d 2> sway.log'

    def install(self):
        #super(SwayRecipe, self).install()
        self.log_dir('install', self.directory, 'sudo install')
        self.run_sudo(self.install_args)

        exe = '%s/bin/sway' % self.prefix_dir
        self.log_dir('install', self.directory, 'setcap cap_sys_ptrace=eip')
        args = ['setcap', 'cap_sys_ptrace=eip', exe]
        self.run_sudo(args)
        self.log_dir('install', self.directory, 'chown root sway')
        args = ['chown', 'root', exe]
        self.run_sudo(args)
        self.log_dir('install', self.directory, 'setuid sway')
        args = ['chmod', '+s', exe]
        self.run_sudo(args)
        self.log_dir('install', self.directory, 'chown root etc/sway/security.d')
        security = os.path.join(self.prefix_dir, 'etc', 'sway', 'security.d')
        args = ['chown', '-R', 'root', security]
        self.run_sudo(args)

        self.log_dir('install', self.directory, 'chmod etc/sway/security.d')
        args = ['chmod', '755', security]
        self.run_sudo(args)
        args = ['chmod', '644', security + '/*']
        self.run_sudo(args)
