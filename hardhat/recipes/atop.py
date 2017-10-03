import os
from .base import GnuRecipe
from ..util import patch


class AtopRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AtopRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '73e4725de0bafac8c63b032e8479e230' \
                      '5e3962afbe977ec1abd45f9e104eb264'
        self.name = 'atop'
        self.version = '2.3.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://atoptool.nl/downloadatop.php'
        self.depends = ['autotools']
        self.url = 'https://atoptool.nl/download/atop-$version.tar.gz'
        self.needs_configure = False
        paths = [
            'BINPATH=%s/bin' % self.prefix_dir,
            'SBINPATH=%s/sbin' % self.prefix_dir,
            'SCRPATH=%s/share/atop' % self.prefix_dir,
            'LOGPATH=%s/var/log/atop' % self.prefix_dir,
            'MAN1PATH=%s/share/man/man1' % self.prefix_dir,
            'MAN5PATH=%s/share/man/man5' % self.prefix_dir,
            'MAN8PATH=%s/share/man/man8' % self.prefix_dir,
            'INIPATH=%s/etc/init.d' % self.prefix_dir,
            'CRNPATH=%s/etc/cron.d' % self.prefix_dir,
            'ROTPATH=%s/etc/logrotate.d' % self.prefix_dir,
            'PMPATH1=%s/lib/pm-utils/sleep.d' % self.prefix_dir,
            'PMPATH2=%s/lib64/pm-utils/sleep.d' % self.prefix_dir,
            'PMPATHD=%s/lib/systemd/system-sleep' % self.prefix_dir]
        self.compile_args = ['make'] + paths
        self.install_args = ['make', 'genericinstall'] + paths

        self.environment['LDFLAGS'] += ' -lncursesw -ltinfow'

    def patch(self):
        src = 'chown root'
        dst = '#chown root'
        file = os.path.join(self.directory, 'Makefile')
        patch(file, src, dst)
