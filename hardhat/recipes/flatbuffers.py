from .base import GnuRecipe
from ..urls import Urls


class FlatbuffersRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlatbuffersRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b81e11aa101927d464a231d6d3b18ab0' \
                      'e8ea4e959b72f415bb385bae0d74df53'

        self.name = 'flatbuffers'
        self.version = '1.3.0'
        self.depends = ['cmake']
        self.url = Urls.github_commit('google', self.name,
                                      'v%s' % self.version)

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
