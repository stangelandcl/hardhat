import os
from .base import GnuRecipe


class OpenJpegRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenJpegRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4ce77b6ef538ef090d9bde1d5eeff8b3' \
                      '069ab56c4906f083475517c2c023dfa7'

        self.name = 'openjpeg'
        self.version = '2.1.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ggreer/the_silver_searcher/' \
                           'releases'
        self.depends = ['cmake', 'doxygen', 'lcms', 'libpng', 'libtiff']
        self.url = 'https://github.com/uclouvain/openjpeg/archive/' \
                   'v$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_VERBOSE_MAKEFILE=ON']

    def install(self):
        super(OpenJpegRecipe, self).install()

        self.log_dir('install', self.directory, 'install man pages')
        script = r'''#!/bin/bash
for man in doc/man/man?/* ; do
    install -v -D -m 644 $man %s/share/$man
done
''' % self.prefix_dir

        filename = os.path.join(self.directory, 'install_man.sh')
        with open(filename, 'wt') as f:
            f.write(script)

        self.run_exe(self.shell_args + [filename],
                     self.directory, self.environment)
