import os
import shutil
from .base import GnuRecipe


class PTunnelRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PTunnelRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a2259bab5fdc06d221832e7273080f6a' \
                      'fc0e1f53d1aedabc96afdb3b2dbd1325'

        self.name = 'ptunnel'
        self.version = '80143798356da92188d4eda763a32c209cc03d3f'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['python']
        self.url = self.github_commit('izderadicka', 'ptunnel')
# usage: python ptunnel.py -d -p jhproxy1.phibred.com:8080 \
#        9993:outlook.office365.com:993

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        shutil.copy2(os.path.join(self.directory, 'src', 'ptunnel.py'),
                     os.path.join(self.prefix_dir, 'bin', 'ptunnel.py'))
