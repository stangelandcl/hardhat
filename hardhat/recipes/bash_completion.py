from .base import GnuRecipe


class BashCompletionRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BashCompletionRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c01f5570f5698a0dda8dc9cfb2a83744' \
                      'daa1ec54758373a6e349bd903375f54d'
        self.name = 'bash-completion'
        self.version = '2.8'
        self.version_url = 'https://github.com/scop/bash-completion/releases'
        self.depends = ['bash']
        self.url = 'https://github.com/scop/$name/releases/download/' \
                   '$version/bash-completion-$version.tar.xz'
