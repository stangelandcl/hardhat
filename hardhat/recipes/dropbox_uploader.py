import os
import shutil
import stat
from .base import GnuRecipe


class DropboxUploaderRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DropboxUploaderRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd7241098758d7ef47c834e27e1080bdf' \
                      '016a6ee973c53947870bbbb773cde883'

        self.name = 'dropbox-uploader'
        self.version = 'c719ac0e327de2b5fd60e898aeb5e3f62a65fb88'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://raw.githubusercontent.com/andreafabrizi/Dropbox-Uploader/$version/dropbox_uploader.sh'

    def extract(self):
        src = self.filename
        dst = os.path.join(self.directory, 'dropbox_uploader.sh')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        shutil.copy2(src, dst)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        dst = os.path.join(self.prefix_dir, 'bin', 'dropbox_uploader.sh')
        shutil.copy2(os.path.join(self.directory, 'dropbox_uploader.sh'),
                     dst)
        os.chmod(dst,
                 stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)

