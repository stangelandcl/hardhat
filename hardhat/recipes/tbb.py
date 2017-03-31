import os
import shutil
from .base import GnuRecipe


class TbbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TbbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '780baf0ad520f23b54dd20dc97bf5aae' \
                      '4bc562019e0a70f53bfc4c1afec6e545'
        self.name = 'tbb'
        self.version = '2017_U5'
        self.version_regex = r'tbb-(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/01org/tbb/releases'
        self.url = 'https://github.com/01org/tbb/archive/$version.tar.gz'

    def configure(self):
        pass


    def install(self):
        dir = os.path.join(self.directory, 'build')
        dirs = os.listdir(dir)
        files = ['libtbbmalloc_proxy.so',
                 'libtbbmalloc_proxy.so.2',
                 'libtbbmalloc.so',
                 'libtbbmalloc.so.2',
                 'libtbb.so',
                 'libtbb.so.2']
        for release in dirs:
            if release.endswith('_release'):
                src = dir
                self.log_dir('install', release, 'installing tbb files')
                for file in files:
                    src_file = os.path.join(dir, release, file)
                    dst_file = os.path.join(self.prefix_dir, 'lib', file)
                    shutil.copy2(src_file, dst_file)
                break
        dir = os.path.join(self.directory, 'include')
        for d in ['serial/tbb', 'tbb']:
            src = os.path.join(dir, d)
            dst = os.path.join(self.prefix_dir, 'include', d)
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
