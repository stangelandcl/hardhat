import os
import shutil
import stat
from .base import JarBase


class TlaToolboxRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(TlaToolboxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None
        self.name = 'tlatoolbox'
        self.version = '1.5.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['java']
        self.url = 'https://github.com/tlaplus/tlaplus/releases/download/' \
                   'v$version/TLAToolbox-$version-linux.gtk.x86_64.zip'

    def clean(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        shutil.copytree(self.directory,
                        os.path.join(self.java_dir, self.name))

        script = r'''#!/bin/sh
%s/tlatoolbox/toolbox "$@"
''' % (self.prefix_dir)

        dst = os.path.join(self.java_dir, 'bin', self.name)
        with open(dst, 'wt') as f:
            f.write(script)

        os.chmod(dst, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
