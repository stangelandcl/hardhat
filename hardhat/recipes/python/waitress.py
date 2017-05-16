from .base import PipBaseRecipe


class WaitressRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WaitressRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c74fa1b92cb183d5a3684210b1bf0a08' \
                      '45fe8eb378fa816f17199111bbf7865f'
                
        self.name = 'waitress'
        self.version = '1.0.2'
