import os
from .base import GnuRecipe


class AcpilightRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AcpilightRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8e02b3efea47ec473826f1362e452fe8' \
                      'ce0e485b2574e469731c92d19269fb09'
        self.name = 'acpilight'
        self.version = '3827fdf18425dba7c5707d102ec16be75b3a86d8'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = self.github_commit('wavexx')
        self.install_args = [
            ['cp', 'xbacklight', '%s/bin/xbacklight' % self.prefix_dir],
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
