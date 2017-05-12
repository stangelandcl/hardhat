from .base import GnuRecipe
from ..version import extension_regex


class SwayRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwayRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6b033a63524dbf1a1770bc0935eb9421' \
                      '775570b7e4b53b81e0f9da5b899025d0'
                
        self.name = 'sway'
        self.depends = ['cairo', 'dmenu', 'fonts',
                        'gdk-pixbuf',
                        'json-c', 'libcap', 'linux-pam', 'pango',
                        'pcre', 'pkgconfig', 'util-linux',
                        'wayland', 'wlc', 'xf86-video-fbdev',
                        'xorg-server']
        # Plus install a specific driver for better performance
        # see recipes/x11/drivers for a list
        # Also install the synaptics driver in that directory
        # for laptop touchpad support
        self.version = 'ee81b1aecb44611f82dc34836ced495ee1514c51'
        self.version_regex = r'(?P<version>\d+\.\d+(-rc\d+)?)' \
            + extension_regex
        self.version_url = 'https://github.com/SirCmpwn/sway/releases'
        self.url = 'https://github.com/SirCmpwn/sway/archive/$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
        self.sudo = True
# to set keyboard layout. run these commands before starting sway
#    export XKB_DEFAULT_LAYOUT=us
#    export XKB_DEFAULT_VARIANT=dvorak

# to run sway with logging 'sway -d 2> sway.log'

    def install(self):
        super(SwayRecipe, self).install()

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
