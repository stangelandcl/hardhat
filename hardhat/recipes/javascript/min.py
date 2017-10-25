import os
import shutil
import stat
from .base import GnuRecipe


class MinRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MinRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cdc3f7e218c9010a1e915185262bdab6' \
                      '22156481a978794857fd53e178235e1c'

        self.name = 'min'
        self.version = '1.6.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['electron', 'grunt']
        self.url = 'https://github.com/minbrowser/min/archive/v$version.tar.gz'

        self.configure_args = [['npm', 'install'],
                               ['npm', 'run', 'buildTranslations']]
        self.compile_args = ['grunt']

    def install(self):
        js = os.path.join(self.prefix_dir, 'js')
        if not os.path.exists(js):
            os.makedirs(js)
        dst = os.path.join(js, 'min')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.move(self.directory, dst)

        text = r'''#!/bin/bash
electron %s
''' % dst

        filename = os.path.join(self.prefix_dir, 'bin', 'min')
        with open(filename, 'wt') as f:
            f.write(text)
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
