import os
from .base import GnuRecipe


class PkgConfigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PkgConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'beb43c9e064555469bd4390dcfd8030b' \
                      '1536e0aa103f08d7abf7ae8cac0cb001'
        self.name = 'pkgconfig'
        self.version = '0.29.1'
        self.url = 'https://pkg-config.freedesktop.org/releases/' \
                   'pkg-config-$version.tar.gz'
        self.build_triplet = self.target_triplet
        self.configure_args = self.shell_args + [
            './configure',
            '--prefix=%s' % (self.prefix_dir),
            '--build=%s' % (self.build_triplet),
            '--target=%s' % (self.target_triplet),
            '--with-internal-glib',
            '--disable-host-tool',
            '--disable-maintainer-mode',
#                                '--with-libiconv=gnu'
            '--with-pc-path=%s/lib/pkgconfig:%s/lib64/pkgconfig:'
            '%s/share/pkgconfig' % (
                self.prefix_dir, self.prefix_dir, self.prefix_dir)
            ]

    def install(self):
        super(PkgConfigRecipe, self).install()

# Add yum completion link to fix warnings
# warnings exist like -bash: /home/stangecl/hardhat/20170507/share/bash-completion/completions/yum: No such file or directory
# due to  /etc/bash_completion.d/yum-utils.bash having this line
# type -t_yum >/dev/null || . $(pkg-config --variable=completionsdir bash-completion)/yum
# but the hardhat pkg-config does not include a yum.bash completion

        self.log_dir('install', self.directory, 'install yum bash completion')
        filename = os.path.join(
            self.prefix_dir,
            'share', 'bash-completion', 'completions', 'yum')
        dir = os.path.dirname(filename)
        if not os.path.exists(dir):
            os.makedirs(dir)

        text = r'''#!/bin/bash

FILE=$(/usr/bin/pkg-config --variable=completionsdir bash-completion)/yum
type -t _yum >/dev/null || [ ! -f $FILE ] || . $FILE
'''

        with open(filename, 'wt') as f:
            f.write(text)
