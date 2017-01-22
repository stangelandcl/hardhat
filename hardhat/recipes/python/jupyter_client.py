from .base import PipBaseRecipe


class JupyterClientRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JupyterClientRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c99a52fac2e5b7a3b714e9252ebf72cb' \
                      'f97536d556ae2b5082baccc3e5cd52ee'

        self.name = 'jupyter_client'
        self.version = '4.4.0'
        self.pydepends = ['pyzmq']
