import os
from .base import GnuRecipe


class AcpilightRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AcpilightRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '82505a58482e353c0ec4f1e6aed2a21d' \
                      '3e209041855332eb539b54a6e3458800'
        self.name = 'acpilight'
        self.version = '1.1'
        self.version_regex = r'v(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'https://gitlab.com/wavexx/acpilight/tags'
        self.url = 'https://gitlab.com/wavexx/acpilight/-/archive/' \
                   'v$version/acpilight-v$version.tar.gz'
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
