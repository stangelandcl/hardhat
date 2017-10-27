import os
from ..base import GnuRecipe


class OpamRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpamRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '888d6258c533f6e1afd274773ea536f6' \
                      '02daa4f8cd47fe0699f17027d294dfed'
        self.name = 'opam'
        self.version = '1.2.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ocaml/opam/' \
                           'releases'
        self.depends = ['autotools', 'ocaml']
        self.url = 'https://github.com/ocaml/opam/releases/download/' \
                   '$version/opam-$version-x86_64-Linux'

    def extract(self):
        pass

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        dst = os.path.join(self.prefix_dir, 'bin', 'opam')
        self.install_args = [
            ['cp', self.filename, dst],
            ['chmod', '+x', dst],
            ['opam', 'init', '--no-setup', '--root=%s/opam' % self.prefix_dir]]

        self.directory = self.prefix_dir
        super(OpamRecipe, self).install()
