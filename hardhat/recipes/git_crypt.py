import os
import shutil
from .base import GnuRecipe


class GitCryptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GitCryptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0a8f92c0a0a125bf768d0c054d947ca4' \
                      'e4b8d6556454b0e7e87fb907ee17cf06'

        self.name = 'git-crypt'
        self.version = '0.5.0'
        self.url = 'https://www.agwa.name/projects/git-crypt/downloads/' \
                   'git-crypt-$version.tar.gz'

        self.install_args += ['ENABLE_MAN=yes']

    def install(self):
        super(GitCryptRecipe, self).install()

        self.log_dir('install', self.directory, 'copy documentation')
        src = '%s/README.md' % self.directory
        dst = '%s/doc/git-crypt.md' % self.prefix_dir
        shutil.copy2(src, dst)
