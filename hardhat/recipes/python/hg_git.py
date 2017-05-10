from .base import PipBaseRecipe


class HgGitRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HgGitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c2a2e46b1891d4e9a991174035d9d17a' \
                      'b5b1416a30f6bcc3144f03807ec636d9'

        self.pythons = ['python2']
        self.depends = ['python-dulwich']
        self.name = 'hg-git'
        self.version = '0.8.6'
