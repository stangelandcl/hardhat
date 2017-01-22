import os
import shutil
from .base import GnuRecipe
from .monkey import MonkeyRecipe
from hardhat.util import patch


class DudaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DudaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ac1f6ced1e469a062784e36293d5dd3' \
                      'bedc5a862016677df6f49be049aa65cc'

        self.name = 'duda'
        self.depends = ['monkey']
        self.version = 'e7763d9dd65c441067ca8d2373950d1cf07dc231'
        self.url = self.github_commit('monkey')
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_BUILD_TYPE=Release',
            '-DWITH_SYSTEM_MALLOC=True',
            '-DCMAKE_VERBOSE_MAKEFILE=ON']

    def patch(self):
        monkey = os.path.join(self.directory, 'deps', 'monkey')
        shutil.rmtree(monkey)

        m = MonkeyRecipe(settings=self)
        self.log_dir('patch', monkey, 'symlink %s->%s'
                     % (m.directory, monkey))
        shutil.copytree(m.directory, monkey)

        src = 'deps/monkey/include'
        dst = '  deps/monkey/include\n' \
              '  deps/monkey/mk_core/include'
        filename = os.path.join(self.directory, 'CMakeLists.txt')
        patch(filename, src, dst)
