import os
import shutil
from .base import GnuRecipe


class RedisPPRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RedisPPRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '33bfc137583a9c5e398a34aaed7bc1c6' \
                      'd48817b488e67a0feccebd5f015d423a'
        self.name = 'redispp'
        self.version = '88b908ac255d43b93132d995bf7770d39496283f'
        self.url = 'https://github.com/brianwatling/redispp/archive/' \
                   '$version.tar.gz'
        self.depends = ['boost']

        self.compile_args += ['libredispp.a', 'libredispp.so']
        self.environment['CXXFLAGS'] += ' -Isrc'

    def install(self):
        self.log_dir('install', self.directory, 'copying files')
        src = os.path.join(self.directory, 'libredispp.so')
        dst = os.path.join(self.prefix_dir, 'lib', 'libredispp.so')
        shutil.copy2(src, dst)

        src = os.path.join(self.directory, 'libredispp.a')
        dst = os.path.join(self.prefix_dir, 'lib', 'libredispp.a')
        shutil.copy2(src, dst)

        src = os.path.join(self.directory, 'src', 'redispp.h')
        dst = os.path.join(self.prefix_dir, 'include', 'redispp.h')
        shutil.copy2(src, dst)

        src = os.path.join(self.directory, 'src', 'redispp.cpp')
        dst = os.path.join(self.prefix_dir, 'src', 'redispp.cpp')
        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))

        shutil.copy2(src, dst)
