import os
import shutil
from .base import GnuRecipe


class CppBTreeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CppBTreeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5653b0f1b7997627a16c402bf1e633ac' \
                      '3e01dff73ff1eaf0ce39935bb0d4e03d'

        self.name = 'cpp-btree'
        self.version = '1.0.1'
        self.version_url = 'https://github.com/google/snappy/releases'
        self.url = 'https://storage.googleapis.com/' \
                   'google-code-archive-downloads/v2/code.google.com/' \
                   'cpp-btree/cpp-btree-$version.tar.gz'
        self.dest_dir = os.path.join(self.prefix_dir, 'include', 'cpp-btree')
        self.install_args = ['cp', '*.h', self.dest_dir]

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        if os.path.exists(self.dest_dir):
            shutil.rmtree(self.dest_dir)
        os.makedirs(self.dest_dir)
        super(CppBTreeRecipe, self).install()
