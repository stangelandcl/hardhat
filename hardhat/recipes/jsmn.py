import os
from .base import GnuRecipe
from ..util import patch


class JsmnRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsmnRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7c25a7da1d36d3fe3071abb4efc9f256' \
                      '3d44a9f215520deed171874f5b353605'

        self.name = 'jsmn'
        self.version = '732d283ee9a2e5c34c52af0e044850576888ab09'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = []
        self.url = self.github_commit('zserge')
        self.install_args = [
            ['cp', 'jsmn.h',
             os.path.join(self.prefix_dir, 'include', 'jsmn.h')],
            ['cp', 'jsmn.c',
             os.path.join(self.prefix_dir, 'src', 'jsmn.c')],
            ['cp', 'libjsmn.a',
             os.path.join(self.prefix_dir, 'lib', 'libjsmn.a')],
            ['mkdir', '-p', os.path.join(self.prefix_dir, 'doc', 'jsmn')],
            ['cp', 'example/*', os.path.join(self.prefix_dir, 'doc', 'jsmn')]
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'enable fast parsing')
        src = '#include <stddef.h>'
        dst = '#include <stddef.h>\n' \
              '#ifndef JSMN_PARENT_LINKS\n' \
              '#define JSMN_PARENT_LINKS\n' \
              '#endif\n'
        filename = os.path.join(self.directory, 'jsmn.h')
        patch(filename, src, dst)

    def configure(self):
        pass
