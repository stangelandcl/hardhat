from .base import PipBaseRecipe


class AsyncTimeoutRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AsyncTimeoutRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b3c0ddc416736619bd4a95ca31de8da6' \
                      '920c3b9a140c64dbef2b2fa7bf521287'
        self.pythons = ['python3']
        self.name = 'async_timeout'
        self.version = '3.0.0'
