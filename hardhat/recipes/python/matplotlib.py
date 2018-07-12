import os
import shutil
from .base import SetupPyRecipe
from hardhat.util import patch


class MatplotlibRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MatplotlibRecipe, self).__init__(*args, **kwargs)
        self.name = 'matplotlib'
        self.version = '2.2.2'
        self.depends = ['cairo', 'gtk3', 'libpng', 'tk']
        self.pydepends = ['cairocffi',
                          'cycler', 'dateutil', 'numpy', 'pillow',
                          'pycairo', 'pygobject', 'pyparsing', 'pytz',
                          'tk']

    def patch(self):
        self.log_dir('patch', self.directory, 'set base dirs to exclude /')
        src = os.path.join(self.directory, 'setup.cfg.template')
        filename = os.path.join(self.directory, 'setup.cfg')
        shutil.copy2(src, filename)

        src = '#basedirlist = /usr'
        dst = 'basedirlist = %s' % self.prefix_dir
        patch(filename, src, dst)
