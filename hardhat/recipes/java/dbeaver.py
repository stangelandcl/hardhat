import os
import shutil
from ..base import GnuRecipe


class DBeaverRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DBeaverRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a3adf0a9090446e4f2bf53d32a217656' \
                      '2ed18ce460a38fc9bdbe81445417da35'

        self.name = 'dbeaver'
        self.depends = ['java']
        self.version = '5.0.4'
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
