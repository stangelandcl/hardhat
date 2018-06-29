from .base import GnuRecipe


class LibTiRpcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTiRpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '86c3a78fc1bddefa96111dd233124c70' \
                      '3b22a78884203c55c3e06b3be6a0fd5e'
        self.name = 'libtirpc'
        self.version = '1.0.3'
        self.url = 'http://downloads.sourceforge.net/project/libtirpc/' \
                   'libtirpc/$version/libtirpc-$version.tar.bz2'
        self.version_url = 'https://sourceforge.net/projects/libtirpc/files/' \
                           'libtirpc/'
        self.version_regex = 'libtirpc/(?P<version>\d+\.\d+\.\d+)/'
        self.depends = ['mit-kerberos']

    def patch(self):
        super(LibTiRpcRecipe, self).patch()
        self.log_dir('patch', self.directory, 'patching for glibc 2.26')

        script = r"""
sed '/stdlib.h/a#include <stdint.h>' -i src/xdr_sizeof.c
sed '/key_secret_is/s/secret/secretkey/' -i src/libtirpc.map
"""
        self.run_patch_script(script)
