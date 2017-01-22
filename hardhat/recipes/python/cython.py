from .base import PipBaseRecipe


class CythonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CythonRecipe, self).__init__(*args, **kwargs)

        self.name = 'cython'
        self.version = '0.25.2'
        self.pypi_name = 'Cython'
        self.sha256 = 'f141d1f9c27a07b5a93f7dc533947206' \
                      '7e2d7140d1c5a9e20112a5665ca60306'
