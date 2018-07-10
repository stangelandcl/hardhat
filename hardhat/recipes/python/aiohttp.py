from .base import PipBaseRecipe


class AioHttpRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AioHttpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f20deec7a3fbaec7b5eb7ad99878427a' \
                      'd2ee4cc16a46732b705e8121cbb3cc12'

        self.pythons = ['python3']
        self.pydepends = ['async_timeout',
                          'attrs',
                          'cchardet',
                          'chardet',
                          'idna-ssl',
                          'multidict',
                          'yarl']
        self.name = 'aiohttp'
        self.version = '3.3.2'
