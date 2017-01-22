from .base import GnuRecipe
from ..cron import add_cron_job


class SysStatRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SysStatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b62fb7609e2f354901f7c384f6aa2022' \
                      '27ca5a7d90af185e6f9d01effd10884b'

        self.name = 'sysstat'
        self.version = '11.5.1'
        self.url = 'https://github.com/sysstat/sysstat/archive/' \
                   'v$version.tar.gz'
        args = ['INIT_DIR=%s/etc/rc.d/init.d' % self.prefix_dir,
                'SYSCONFIG_DIR=%s/etc/sysconfig' % self.prefix_dir]
        self.configure_args += ['--disable-file-attr',
                                'sa_dir=%s/var/log/sa' % self.prefix_dir,
                                'rcdir=%s/etc/rc.d' % self.prefix_dir,
                                ]
        self.compile_args += args
        self.install_args += args

    def install(self):
        super(SysStatRecipe, self).install()

        jobs = [  # Run system activity accounting tool every 10 minutes
                ('system_activity_update',
                 '*/10 * * * * %s/lib64/sa/sa1 1 1' % self.prefix_dir),
                # Generate a daily summary of process accounting at 23:53
                ('system_activity_summary',
                 '53 23 * * * %s/lib64/sa/sa2 -A' % self.prefix_dir),
                # reset the collector on reboot
                ('system_activity_reboot',
                 '@reboot %s/lib64/sa/sa1 --boot' % self.prefix_dir)
                ]

        for name, job in jobs:
            add_cron_job(name, job, self.environment)
