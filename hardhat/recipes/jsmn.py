import os
from .base import GnuRecipe
from ..util import patch


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '422be63017eb7afdf1c0be4fcb0f7be7' \
                      '40447b7e6dbec99f6121491d7a11b3bb'

        self.name = 'jsmn'
        self.version = '436a26632d657917c2bcc4e24bfb67644d59887a'
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
