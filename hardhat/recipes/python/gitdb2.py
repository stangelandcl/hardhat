from .base import PipBaseRecipe


class GitDB2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GitDB2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b60e29d4533e5e25bb50b7678bbc187c' \
                      '8f6bcff1344b4f293b2ba55c85795f09'
        self.name = 'gitdb2'
        self.version = '2.0.3'
        self.pydepends = ['smmap2']
