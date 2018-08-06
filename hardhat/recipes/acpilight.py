import os
from .base import GnuRecipe


class AcpilightRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AcpilightRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2253722a0abb0bc6beef1eddf0270e57' \
                      '13e78b766769cd778246f9437c43e546'
        self.name = 'acpilight'
        self.version = 'f54865ed9a11eedaeffa71af320a3bf36c89f15d'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://gitlab.com/wavexx/acpilight/-/archive/$version/' \
                   'acpilight-$version.tar.gz'
        self.install_args = [
            ['cp', 'xbacklight', '%s/bin/xbacklight' % self.prefix_dir],
            ['cp', 'xbacklight', '%s/bin/acpilight' % self.prefix_dir],
            ['mkdir', '-p', '%s/man/man1' % self.prefix_dir],
            ['cp', 'xbacklight.1', '%s/man/man1' % self.prefix_dir]
            ]
        self.sudo = True

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        super(AcpilightRecipe, self).install()
        ## udev does not work even though acpilight recommends it
        #dst = '/etc/udev/rules.d/90-backlight.rules'
        #src = '90-backlight.rules'
        #self.run_sudo(['cp', src, dst])

        # Instead add current user to video group and make video group owner of
        # backlight
        self.run_sudo(['chown', 'root:video',
                      '/sys/class/backlight/*/brightness'])
        self.run_sudo(['chmod', 'g+w',
                      '/sys/class/backlight/*/brightness'])
        self.run_sudo(['usermod', '-a', '-G', 'video',
                       os.environ['USER']])
        self.log_dir('install', self.directory,
                     'if user was not already in video group then a'
                     ' re-login is required to use xbacklight')
