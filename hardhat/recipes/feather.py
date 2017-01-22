from .base import GnuRecipe
import os


class FeatherRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FeatherRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3bd7988896f40e4a08989060dafb5d34' \
                      'bd242cca88c0da7996f418f84a5892cd'

        self.name = 'feather'
        self.version = 'c156483ba4a738ee69d1d135efe7edc32dc7bce8'
        self.depends = ['googletest', 'flatbuffers']
        self.url = self.github_commit('wesm')

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def configure(self):
        self.directory = os.path.join(self.directory, 'cpp')
        super(FeatherRecipe, self).configure()
