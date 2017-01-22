import os
from .base import GnuRecipe


class ICURecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ICURecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2b0a4410153a9b20de0e20c7d8b66049' \
                      'a72aef244b53683d0d7521371683da0c'

        self.name = 'icu'
        self.version = '58.2'
        self.version_regex = '(?P<version>\d+\.\d+)/'
        self.version_url = 'http://download.icu-project.org/files/icu4c/'
        underscore_version = self.version.replace('.', '_')
        self.url = 'http://download.icu-project.org/files/icu4c/$version/' \
            'icu4c-%s-src.tgz' % (underscore_version)

        # ICU requires a working host ICU to cross-compile
        self.configure_strip_cross_compile()
        self.environment_strip_lto()
        self.environment['CXXFLAGS'] += ' -fvisibility=default'
        self.environment['CFLAGS'] += ' -fvisibility=default'
        self.environment['LDFLAGS'] += ' -fvisibility=default'


    def clean(self):
        super(ICURecipe, self).clean()
        self.log_dir('clean', self.directory, 'removing old libicus')
        files = ['libicudata',
                 'libicui18n',
                 'libicuio',
                 'libicule',
                 'libiculx',
                 'libicutest',
                 'libicutu',
                 'libicuuc']
        dir = os.path.join(self.prefix_dir, 'lib')
        for file in files:
            args = ['rm', '-f', file + '.*']
            self.run_exe(args, dir, self.environment)

    def patch(self):
        self.directory = os.path.join(self.directory, 'source')
