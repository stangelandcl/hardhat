import os
import shutil
from .base import GnuRecipe


class FastCppCsvParserRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FastCppCsvParserRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5e2beea28f8e85f8e26a37e5a34ff918' \
                      '0f817f75049d5bf395ab6e0759c7f8ca'

        self.name = 'fastcppcsvparser'
        self.version = '9bf299cefb60d0e4ba7dc79d51491595ab1b3213'
        self.url = self.github_commit('ben-strasser', 'fast-cpp-csv-parser')

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.prefix_dir, 'installing fastppcsvparser')
        destdir = os.path.join(self.prefix_dir, 'include', 'fastcppcsvparser')
        os.makedirs(destdir)
        src = os.path.join(self.directory, 'csv.h')
        dst = os.path.join(destdir, 'csv.h')
        shutil.copy2(src, dst)
