import os
from .base import GnuRecipe
from ..util import patch


class CJsonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CJsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6d1482c1b492893b25ab7e77ee6098fe' \
                      '3ef10585df660e5ffe67e632a8c5b9e4'

        self.name = 'cJSON'
        self.version = '1.5.2'
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


class Mingw64CJsonRecipe(CJsonRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64CJsonRecipe, self).__init__(*args, **kwargs)
        self.name = 'mingw64-cjson'
        self.environment['CFLAGS'] += ' -D__WINDOWS__'
        extra = ['SHARED=dll']
        self.compile_args += extra
        self.install_args += extra
