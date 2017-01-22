from .base import PipBaseRecipe


class HgGitRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HgGitRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python2']
        self.depends = ['python-dulwich']
        self.name = 'hg-git'
        self.version = '0.8.5'
        self.sha256 = 'f5cab3cc610926458733a2321ad3df5a' \
                      '7c56870bbf0c6d962dfa742e6ea04782'
