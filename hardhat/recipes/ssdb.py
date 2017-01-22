import os
from .base import GnuRecipe


class SsdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SsdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3feffa31c07bc3b288978eb0a54ba64a' \
                      '72cb7ee56949faa5cd361ad1a3151111'

        self.name = 'ssdb'
        self.description = 'client-server key value database in C++'
        self.version = '1.9.2'
        self.url = self.github_commit('ideawu')
        self.ssdb_dir = os.path.join(self.prefix_dir, 'ssdb')
        self.compile_args += ['PREFIX=%s' % self.ssdb_dir]
        self.install_args += ['PREFIX=%s' % self.ssdb_dir]

    def post_install(self):
        self.log_dir('post_install', self.ssdb_dir, 'symlinking files')
        for file in ['ssdb-bench',
                     'ssdb-cli',
                     'ssdb-cli.cpy',
                     'ssdb-dump',
                     'ssdb-repair',
                     'ssdb-server']:
            src = os.path.join(self.prefix_dir, 'ssdb', file)
            dst = os.path.join(self.prefix_dir, 'bin', file)
            if os.path.exists(dst):
                os.remove(dst)
            os.symlink(src, dst)
