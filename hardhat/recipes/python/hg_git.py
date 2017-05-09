from .base import PipBaseRecipe


class HgGitRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HgGitRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python2']
        self.depends = ['python-dulwich']
        self.name = 'hg-git'
        self.version = '0.8.6'
