from .base import PipBaseRecipe


class PasslibRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PasslibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3d948f64138c25633613f303bcc47112' \
                      '6eae67c04d5e3f6b7b8ce6242f8653e0'
                
        self.name = 'passlib'
        self.version = '1.7.1'
