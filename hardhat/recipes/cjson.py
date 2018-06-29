import os
from .base import GnuRecipe
from ..util import patch


class CJsonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CJsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6eb9d852a97ffbe149e747f54d63e39a' \
                      '674fa248bb24902a14c079803067949a'

        self.name = 'cJSON'
        self.version = '1.7.7'
        self.url = 'https://github.com/DaveGamble/cJSON/archive/' \
                   'v$version.tar.gz'
        self.version_regex = 'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.version_url = 'https://github.com/DaveGamble/cJSON/releases'
        self.compile_args = ['make', 'all']
        self.install_args = [
            self.install_args + ['PREFIX=""',
                                 'DESTDIR=%s' % self.prefix_dir,
                                 'LIBRARY_PATH=lib',
                                 'INCLUDE_PATH=include/cjson'],
            ['cp', 'libcjson.a', '%s/lib' % self.prefix_dir],
            ['cp', 'libcjson_utils.a', '%s/lib' % self.prefix_dir]]

    def patch(self):
        filename = os.path.join(self.directory, 'Makefile')
        src = 'CFLAGS += -fstack-protector-strong'
        dst = 'CFLAGS +='
        patch(filename, src, dst)

    def configure(self):
        pass
