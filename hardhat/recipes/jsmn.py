import os
from .base import GnuRecipe


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f40d98aa140ad16e56128476924d7042' \
                      '733f276383d2e1d26d206e51c8f1d939'
        self.name = 'jsmn'
        self.version = 'a81db82332c7a8c50e41deb491459338f219f221'
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
