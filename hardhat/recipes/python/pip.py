from .base import SetupPyRecipe


class PipRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a0e11645ee37c90b40c46d607070c4fd' \
                      '583e2cd46231b1c06e389c5e814eed76'

        self.name = 'pip'
        self.version = '18.0'
        self.url = 'https://files.pythonhosted.org/packages/69/81/' \
                   '52b68d0a4de760a2f1979b0931ba7889202f302072cc7a0d614211bc7579/pip-$version.tar.gz'
