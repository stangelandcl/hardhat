from .base import GnuRecipe


class MLKitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MLKitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c6adbeb9a85f7b3586d0961fd3b170f' \
                      'f31e09fa0ff12889b76b9ceb459059c4'

        self.description = 'SML compiler'
        self.name = 'mlkit'
        self.version = '4.3.9'
        self.url = 'https://github.com/melsman/mlkit/archive/' \
                   'mlkit-$version.tar.gz'
