import os
import shutil
from ..base import GnuRecipe


class DBeaverRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DBeaverRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '38a9a4388a75590c178fbcb505b0856c' \
                      '3c3bf684450d10070f8bdc5c8ecc4d4d'
                
        self.name = 'dbeaver'
        self.depends = ['java']
        self.version = '4.2.3'
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
