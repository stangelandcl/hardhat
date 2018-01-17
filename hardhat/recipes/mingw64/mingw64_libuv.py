import os
from .base import Mingw64BaseRecipe
from hardhat.util import patch


class Mingw64LibUVRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64LibUVRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '17afc94ec307be28fe8d431667917121' \
                      '9770df4f993905a79643c7583e106489'


        self.name = 'mingw64-libuv'
        self.version = '1.15.0'
        self.url = 'https://github.com/libuv/libuv/archive/v$version.tar.gz'
        self.configure_args = [
            ['./autogen.sh'],
            self.configure_args]

    def patch(self):
        self.log_dir('patch', self.directory, 'patching')
        src = '#include <iphlpapi.h>'
        dst = '#include <wincrypt.h>\n#include <iphlpapi.h>'
        filename = os.path.join(self.directory, 'src/win/util.c')
        patch(filename, src, dst)
