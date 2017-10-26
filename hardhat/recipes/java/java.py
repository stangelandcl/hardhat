import os
from ..base import GnuRecipe


class OracleJreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OracleJreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c697fe1b8ef4d93ffb2c944c3b38b64' \
                      '697f5427c183f659e527a6fecccd789f'

        self.name = 'java'
        self.version = '8u151'
        self.depends = ['rsync']
        self.url = 'hg:java/jre-$version-linux-x64.tar.gz'
        self.install_args = [
            ['rm', '-rf', '%s/java/man' % self.prefix_dir],
            ['rsync', '-av',
             '%s/' % self.directory,
            '%s/' % (os.path.join(self.prefix_dir, 'java'))]]

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
