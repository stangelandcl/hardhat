import os
import shutil
import stat
from ..base import GnuRecipe


class JarBase(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JarBase, self).__init__(*args, **kwargs)
        self.depends = ['java']

    def extract(self):
        pass

    def clean(self):
        if os.path.exists(self.installed_file):
            os.remove(self.installed_file)

    def configure(self):
        pass

    def compile(self):
        pass

    @property
    def java_dir(self):
        if hasattr(self, '_java_dir'):
            return self._java_dir
        return os.path.join(self.prefix_dir, 'java')

    @java_dir.setter
    def java_dir(self, value):
        self._java_dir = value

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        shutil.copy2(self.filename, self.installed_file)

        java = os.path.join(self.java_dir, 'bin', 'java')
        script = r'''#!/bin/sh
%s -jar %s "$@"
''' % (java, self.installed_file)

        dst = os.path.join(self.java_dir, 'bin', self.name)
        with open(dst, 'wt') as f:
            f.write(script)

        os.chmod(dst, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
