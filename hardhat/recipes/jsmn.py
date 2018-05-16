import os
from .base import GnuRecipe
from ..util import patch


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fece72c9061d02335645f9ad798f682b' \
                      '392920474eb6bd8e65140c126b65f790'

        self.name = 'jsmn'
        self.version = '0cced93d5fd01fbb1839e290bc8757d29b8d99bf'
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
