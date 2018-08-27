from .base import GnuRecipe
from ..urls import Urls


class LibPipelineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPipelineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0d72e12e4f2afff67fd7b9df0a24d7ba' \
                      '42b5a7c9211ac5b3dcccc5cd8b286f2b'
        self.name = 'libpipeline'
        self.version = '1.5.0'
        self.url = Urls.savannah(self.name, self.version)
