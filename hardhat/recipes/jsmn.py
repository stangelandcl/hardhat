import os
from .base import GnuRecipe


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '12081fdc46775a265798ccbb12d82b65' \
                      '2bc9c97fd2df106b48f5cc46025da5e9'

        self.name = 'jsmn'
        self.version = 'f33cb55e99c011f499ab636b32c006c819ddf0cd'
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
