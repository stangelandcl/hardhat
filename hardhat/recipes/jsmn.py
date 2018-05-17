import os
from .base import GnuRecipe
from ..util import patch


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c57270b93ca57cbcf06bfbfed706a03d' \
                      'd82859b65b74dc07a750eba88aa56e29'
        self.name = 'jsmn'
        self.version = '48ab2985a9265b10dbd89b729fbd50953f4e4470'
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
