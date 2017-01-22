from .base import GnuRecipe


class BashCompletionRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BashCompletionRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c0f76b5202fec9ef8ffba82f5605025c' \
                      'a003f27cfd7a85115f838ba5136890f6'

        self.name = 'bash-completion'
        self.version = '2.4'
        self.version_url = 'https://github.com/scop/bash-completion/releases'
        self.depends = ['bash']
        self.url = 'https://github.com/scop/$name/releases/download/' \
                   '$version/bash-completion-$version.tar.xz'
