import os
import shutil
from .base import GnuRecipe


class GoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47fda42e46b4c3ec93fa5d4d4cc6a748' \
                      'aa3f9411a2a2b7e08e3a6d80d753ec8b'

        self.name = 'go'
        self.version = '1.7.4'
        self.url = 'https://storage.googleapis.com/golang/go$version.linux-amd64.tar.gz'
        self.install_dir = os.path.join(self.prefix_dir, 'go')

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory,
                     'copying to %s' % self.install_dir)
        if os.path.exists(self.install_dir):
            shutil.rmtree(self.install_dir)
        shutil.copytree(self.directory, self.install_dir)

        
