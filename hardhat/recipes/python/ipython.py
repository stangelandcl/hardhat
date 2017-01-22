from .base import PipBaseRecipe


class IPythonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IPythonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ef4694e1345913182126b219aaa4a00' \
                      '47e191af414256da6772cf249571b961'

        self.name = 'ipython'
        self.pydepends = ['decorator',
                          'pexpect',
                          'pickleshare', 'prompt-toolkit',
                          'setuptools',
                          'simplegeneric', 'traitlets']
        self.version = '5.1.0'
