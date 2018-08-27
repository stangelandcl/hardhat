from .base import SetupPyRecipe


class AioHttpRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(AioHttpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9b15efa7411dcf3b59c1f4766eb16ba1' \
                      'aba4531a33e54d469ee22106eabce460'

        self.pythons = ['python3']
        self.pydepends = ['async_timeout',
                          'attrs',
                          'cchardet',
                          'chardet',
                          'idna-ssl',
                          'multidict',
                          'yarl']
        self.name = 'aiohttp'
        self.version = '3.4.0'
        self.url = 'https://files.pythonhosted.org/packages/09/01/22c9b713b195d071b73fdc2f977f8717497b0d30c41c0b4a9cd908b925ec/aiohttp-3.4.0.tar.gz'
