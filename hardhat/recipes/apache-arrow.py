from .base import GnuRecipe
import os


class ApacheArrowRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ApacheArrowRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2094cc6492e77ede19937375769de105' \
                      '603a50440a6257fefd4038f1176a0626'
        self.name = 'apache-arrow'
        self.version = '0.10.0'
        self.depends = ['cmake', 'flatbuffers', 'googletest']
        self.url = 'https://github.com/apache/arrow/archive/' \
                   'apache-arrow-$version.tar.gz'
        self.version_url = 'https://github.com/apache/arrow/releases'
        self.version_regex = r'''apache\-arrow\-(?P<version>\d+\.\d+\.\d+)'''

        self.environment['GTEST_HOME'] = self.prefix_dir
        self.environment['FLATBUFFERS_HOME'] = self.prefix_dir

        self.configure_args = ['cmake', '..',
                               '-DCMAKE_BUILD_TYPE=Release',
                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir]

    def patch(self):
        dir = os.path.join(self.directory, 'cpp', 'release')
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.directory = dir
