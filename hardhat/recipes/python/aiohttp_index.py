from .base import PipBaseRecipe


class AioHttpIndexRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AioHttpIndexRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.pydepends = ['aiohttp']
        self.name = 'aiohttp-index'
        self.version = '0.1'
        self.sha256 = '45e9f6ac49974d8893084f7e07a294a1' \
                      '5d3b41b313cc06e2993d922e12782864'
