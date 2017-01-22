import os
import shutil
from ..base import GnuRecipe


class DBeaverRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DBeaverRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e71499b016ff667b5ab5514f69560629' \
                      'd027a0a87999aaf6a7592212ad4d7c2a'

        self.name = 'dbeaver'
        self.depends = ['java']
        self.version = '3.8.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://dbeaver.jkiss.org/files/'
        self.url = 'http://dbeaver.jkiss.org/files/$version/' \
                   'dbeaver-ce-$version-linux.gtk.x86_64.tar.gz'

    def clean(self):
        java = os.path.join(self.prefix_dir, 'java')
        dir = os.path.join(java, 'dbeaver')
        if os.path.exists(dir):
            shutil.rmtree(dir)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        java = os.path.join(self.prefix_dir, 'java')
        dir = os.path.join(java, 'dbeaver')
        shutil.copytree(self.directory, dir)
        src = os.path.join(dir, 'dbeaver')
        dst = os.path.join(java, 'bin', 'dbeaver')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
