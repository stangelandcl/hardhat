import os
import shutil
from ..base import GnuRecipe


class OracleJreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OracleJreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f2249370a6ac4ca8977b66d7665179f0' \
                      'fef4df732f3af80b0f34567d594588bf'
        self.name = 'java'
        self.version = '8u66'
        self.rebuilds = ['graphviz']
        self.depends = ['rsync']
        self.url = 'hg:pkgsrc/2015Q4/distfiles/jre-$version-linux-x64.tar.gz'

    def do_download(self, tmpfile):
        args = [
            'rsync',
            '-av',
            self.url,
            tmpfile
            ]
        dir = os.path.dirname(tmpfile)
        self.run_exe(args, dir, self.environment)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        dir = os.path.join(self.prefix_dir, 'java')
        shutil.copytree(self.directory, dir)
