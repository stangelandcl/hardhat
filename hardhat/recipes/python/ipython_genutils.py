from .base import PipBaseRecipe


class IPythonGenutilsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IPythonGenutilsRecipe, self).__init__(*args, **kwargs)

        self.name = 'ipython-genutils'
        self.version = '0.1.0'
        self.sha256 = '3a0624a251a26463c9dfa0ffa635ec51' \
                      'c4265380980d9a50d65611c3c2bd82a6'
