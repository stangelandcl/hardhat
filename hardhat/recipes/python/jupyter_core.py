from .base import PipBaseRecipe


class JupyterCoreRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JupyterCoreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '89c55399c8437f777197c2c82c1ff563' \
                      '9c7f71d4eb2f172a81afa120b68dc7b3'

        self.name = 'jupyter_core'
        self.version = '4.2.1'
