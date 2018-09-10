import os
import shutil
from .base import GnuRecipe
from ..util import patch


class GitLfsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GitLfsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9565fa9c2442c3982567a3498c9352cd' \
                      'a88e0f6a982648054de0440e273749e7'
        self.name = 'git-lfs'
        self.version = '2.5.1'
        self.depends = ['git']
        self.url = 'https://github.com/git-lfs/git-lfs/releases/' \
                   'download/v$version/git-lfs-linux-amd64-v$version.tar.gz'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copying git-lfs to bin')
        shutil.copy2(os.path.join(self.directory, 'git-lfs'),
                     os.path.join(self.prefix_dir, 'bin', 'git-lfs'))

        self.log_dir('install', self.directory, 'installing git-lfs')
        self.run_exe(['git', 'lfs', 'install'],
                     self.directory, self.environment)

        self.log_dir('install', self.directory, 'patching .gitconfig')
        config = os.path.join(os.environ["HOME"], ".gitconfig")
        patch(config, r'	process = git-lfs filter-process',
                      r'#	process = git-lfs filter-process')
