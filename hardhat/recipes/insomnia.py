import os
import shutil
import stat
from .base import GnuRecipe


class InsomniaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(InsomniaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9d5a67ef908f1ca68b736e5f547d166' \
                      '0a69f8cb2a14900998e942608da1c562'

        self.name = 'insomnia'
        self.version = '5.16.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ggreer/the_silver_searcher/' \
                           'releases'
        self.url = 'https://github.com/getinsomnia/insomnia/releases/' \
                   'download/v$version/insomnia-$version-x86_64.AppImage'

    def extract(self):
        pass

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy to bin')
        dst = os.path.join(self.prefix_dir, 'bin', 'insomnia')
        shutil.copy2(self.filename, dst)
        os.chmod(dst,
                 stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)
