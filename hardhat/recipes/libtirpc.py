from .base import GnuRecipe


class LibTiRpcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTiRpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '723c5ce92706cbb601a8db09110df1b4' \
                      'b69391643158f20ff587e20e7c5f90f5'

        self.name = 'libtirpc'
        self.version = '1.0.2'
        self.url = 'http://downloads.sourceforge.net/project/libtirpc/' \
                   'libtirpc/$version/libtirpc-$version.tar.bz2'
        self.depends = ['mit-kerberos']

    def patch(self):
        super(LibTiRpcRecipe, self).patch()
        self.log_dir('patch', self.directory, 'patching for glibc 2.26')

        script = r"""
sed '/stdlib.h/a#include <stdint.h>' -i src/xdr_sizeof.c
sed '/key_secret_is/s/secret/secretkey/' -i src/libtirpc.map
"""
        self.run_patch_script(script)
