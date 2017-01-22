from .base import PipBaseRecipe


class AioHttpRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AioHttpRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.pydepends = ['cchardet', 'chardet', 'multidict']
        self.name = 'aiohttp'
        self.version = '0.22.5'
        self.sha256 = '9c51af030c866f91e18a219614e39d34' \
                      '5db4483ed9860389d0536d74d04b0d3b'
