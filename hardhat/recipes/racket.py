import os
import shutil
from .base import GnuRecipe


class RacketRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RacketRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bf2bce50b02c626666a8d2093638893e' \
                      '8beb8b2a19cdd43efa151a686c88edcf'

        self.depends = ['libffi']
        self.name = 'racket'
        self.version = '6.6'
        self.url = 'http://mirror.racket-lang.org/installers/$version/' \
                   'racket-$version-src.tgz'

        self.configure_args = self.shell_args + [
            '../src/configure',
            '--prefix=%s' % self.prefix_dir]
        # -O3 generates SIGSEGVs
        self.environment['CFLAGS'] = '-O2'
        self.environment['CXXFLAGS'] = '-O2'

    def patch(self):
        self.directory = os.path.join(self.directory, 'build')
        os.makedirs(self.directory)

    def clean(self):
        super(RacketRecipe, self).clean()

        dirs = ['include', 'etc', 'share/doc', 'share', 'lib']
        for dir in dirs:
            d = os.path.join(self.prefix_dir, dir, 'racket')
            if os.path.exists(d):
                shutil.rmtree(d)
