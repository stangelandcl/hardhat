from .base import PipBaseRecipe


class JupyterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JupyterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9dc4b3318f310e34c82951ea5d6683f' \
                      '67bed7def4b259fafbfe4f1beb1d8e5f'

        self.name = 'jupyter'
        self.pydepends = ['jupyter_console',
                          'notebook', 'qtconsole']
        self.version = '1.0.0'
