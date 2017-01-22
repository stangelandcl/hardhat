import os
from .base import SetupPyRecipe
from hardhat.util import patch


class PySideRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PySideRecipe, self).__init__(*args, **kwargs)

        self.depends = ['qt5']
        self.name = 'pyside'
        self.pypi_name = 'PySide'
        self.version = '1.2.4'
        self.sha256 = '1421bc1bf612c396070de9e1ffe227c0' \
                      '7c1f3129278bc7d30c754b5146be2433'

        # To disable warnings for std::auto_ptr<>
        self.environment.CFLAGS += ' -Wno-deprecated-declarations'
        self.environment.CXXFLAGS += ' -Wno-deprecated-declarations'

    def patch(self):
        self.log_dir('patch', self.directory, 'add Python 3.5 support')
        filename = os.path.join(self.directory, 'setup.py')

        src = "        'Programming Language :: Python :: 3.4',"
        dst = "        'Programming Language :: Python :: 3.4',\n" \
              "        'Programming Language :: Python :: 3.5',"
        patch(filename, src, dst)
