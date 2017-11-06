import os
from .base import GnuRecipe
from ..util import patch


class RTagsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RTagsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c860c0f659a5d514543afda1a657ed0d' \
                      'a108455c1cee414803f726e7d21d2975'
        self.name = 'rtags'
        self.version = 'e413e31d1e74fae1fc1bf86792013c3680be6580'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['cmake', 'llvm', 'rct']
        self.url = self.github_commit('Andersbakken')
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_EXPORT_COMPILE_COMMANDS=1',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DFORCE_BASH_COMPLETION_INSTALLATION=ON']

    def patch(self):
        self.log_dir('patch', self.directory, 'patching cmakelists')
        src = 'include(rct/rct.cmake)'
        dst = r'''include(%s/lib/cmake/rct.cmake)''' % self.prefix_dir

        filename = os.path.join(self.directory, 'src', 'CMakeLists.txt')
        patch(filename, src, dst)
