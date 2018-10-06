import os
import shutil
from .base import GnuRecipe


class ClocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ClocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '082f53530eee3f9ee84ec449eca59a77' \
                      'ff114250cd7daf9519679537b5b21d67'

        self.name = 'cloc'
        self.version = '1.80'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/AlDanial/cloc/releases'
#        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/AlDanial/cloc/releases/download/' \
                   'v$version/cloc-$version.tar.gz'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy cloc to bin')
        src = os.path.join(self.directory, 'cloc')
        dst = os.path.join(self.prefix_dir, 'bin', 'cloc')

        shutil.copy2(src, dst)
