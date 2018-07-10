from .base import PipBaseRecipe


class ZStandardRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ZStandardRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '59c7d6f1f85cebb5124abb50d8ec281c' \
                      '5311e0812e18785e28b197cf1515dd3b'

        self.name = 'zstandard'
        self.depends = ['zstd']
        self.pydepends = ['cffi']
        self.version = '0.9.1'
        self.extra_install_args = ['--system-zstd']
