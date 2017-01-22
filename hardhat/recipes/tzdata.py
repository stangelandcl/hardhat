import os
import stat
from .base import GnuRecipe


class TzDataRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TzDataRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f5ee4e0f115f6c2faee1c4b16193a973' \
                      '38cbd1b503f2cea6c5a768c82ff39dc8'

        self.name = 'tzdata'
        self.version = '2016j'
        self.version_regex = r'(?P<version>\d\d\d\d[a-z])'
        self.url = 'https://www.iana.org/time-zones/repository/releases/' \
                   'tzdata$version.tar.gz'
        self.install_file = os.path.join(self.directory, 'install.sh')
        self.install_args = ['sh', self.install_file]

    def patch(self):
        script = r'''#!/bin/bash
ZONEINFO="%s/%s/share/zoneinfo"
mkdir -pv $ZONEINFO/{posix,right}

for tz in etcetera southamerica northamerica europe africa antarctica  \
          asia australasia backward pacificnew systemv; do
    zic -L /dev/null   -d $ZONEINFO       -y "sh yearistype.sh" ${tz}
    zic -L /dev/null   -d $ZONEINFO/posix -y "sh yearistype.sh" ${tz}
    zic -L leapseconds -d $ZONEINFO/right -y "sh yearistype.sh" ${tz}
done

cp -v zone.tab zone1970.tab iso3166.tab $ZONEINFO
zic -d $ZONEINFO -p America/Chicago
unset ZONEINFO
''' % (self.prefix_dir, self.target_triplet)

        with open(self.install_file, 'wt') as f:
            f.write(script)
        os.chmod(self.install_file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)

    def configure(self):
        pass

    def compile(self):
        pass
