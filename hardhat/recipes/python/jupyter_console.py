from .base import PipBaseRecipe


class JupyterConsoleRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JupyterConsoleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ddfc8cc49921b0ed852500928922e63' \
                      '7f9188358c94b5c76339a5a8f9ac4c11'

        self.name = 'jupyter_console'
        self.version = '5.0.0'
