from .base import PipBaseRecipe


class PyGit2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PyGit2Recipe, self).__init__(*args, **kwargs)

        self.depends = ['libgit2']
        self.name = 'pygit2'
        self.version = '0.24.0'
