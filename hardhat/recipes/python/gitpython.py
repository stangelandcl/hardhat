from .base import PipBaseRecipe


class GitPythonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GitPythonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ad61bc25deadb535b047684d06f3654c' \
                      '001d9415e1971e51c9c20f5b510076e9'
        self.name = 'gitpython'
        self.version = '2.1.8'
        self.pydepends = ['gitdb2']
