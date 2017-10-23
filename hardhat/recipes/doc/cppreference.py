import os
import shutil
import stat
from ..base import TarballRecipe


class CppReferenceRecipe(TarballRecipe):
    def __init__(self, *args, **kwargs):
        super(CppReferenceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ea830dd6e12a9278a26a383f11ee1ebd' \
                      '7d898c4c8bbfd1da6ad2311d201da1c8'

        self.name = 'cppreference'
        self.version = '20161029'
        self.url = 'http://upload.cppreference.com/mwiki/images/4/4c/' \
                   'html_book_$version.tar.gz'

    def configure(self):
        pass

    def install(self):
        dir = os.path.join(self.prefix_dir, 'doc', self.name)
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)
        SCRIPT=r'''#!/bin/bash

firefox %s/index.html

''' % dir

        script = os.path.join(self.prefix_dir, 'bin', 'cppreference')
        with open(script, 'wt') as f:
            f.write(SCRIPT)
        os.chmod(script,
                 stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)
