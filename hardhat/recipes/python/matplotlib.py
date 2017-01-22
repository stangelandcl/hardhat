from .base import PipBaseRecipe


class MatplotlibRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MatplotlibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a0a5dc39f785014f2088fed2c6d2d129' \
                      'f0444f71afbb9c44f7bdf1b14d86ebbc'

        self.name = 'matplotlib'
        self.version = '1.5.3'
        self.depends = ['cairo', 'gtk3', 'libpng', 'tk']
        self.pydepends = ['cairocffi',
                          'cycler', 'dateutil', 'numpy', 'pillow',
                          'pycairo', 'pygobject', 'pyparsing', 'pytz',
                          'tk']
