import os
from .base import GnuRecipe
from ..util import patch


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '07a6a8cf12cc1ec736307e5db837bb1b' \
                      '937f794c2fe84a6d46809b14a9c053b1'
        self.name = 'jsmn'
        self.version = '4df8b4fd2b13a056fe2a38cf66e2b088d36e8e20'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = []
        self.url = self.github_commit('stangelandcl')
        self.install_args = [
            ['make', 'install', 'PREFIX=' + self.prefix_dir],
            ['mkdir', '-p', os.path.join(self.prefix_dir, 'doc', 'jsmn')],
            ['cp', 'example/*', os.path.join(self.prefix_dir, 'doc', 'jsmn')]
            ]

    def configure(self):
        pass
