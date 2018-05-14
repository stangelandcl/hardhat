import os
from .base import GnuRecipe
from ..util import patch


class CJsonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CJsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd1ca2665b34fea164a877637b4ad1624' \
                      'aa23390fe75de91b88e18c5d6ec91978'
                                        
        self.name = 'cJSON'
        self.version = '1.7.6'
        self.url = 'https://github.com/DaveGamble/cJSON/archive/' \
                   'v$version.tar.gz'
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
