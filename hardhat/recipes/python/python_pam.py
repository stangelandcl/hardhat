from .base import PipBaseRecipe


class PythonPamRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonPamRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '26efe4e79b869b10f97cd8c4a6bbb04a' \
                      '4e54d41186364e975b4108c9c071812c'
        self.depends = ['linux-pam']
        self.name = 'python-pam'
        self.version = '1.8.2'
