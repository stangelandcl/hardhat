import os
import shutil
import stat
from .base import GnuRecipe


class GoProVRRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GoProVRRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5971ea8b00df56979d30a19aaacf4b7e' \
                      '805c75ca0b59a637fe58efd9940a6f72'

        self.name = 'goprovr'
        self.version = '220_2017-02-13'
        self.url = 'http://download.kolor.com/ked/stable/linux64tarxz'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy dir')
        dst = os.path.join(self.prefix_dir, 'goprovr')
        if os.path.exists(dst):
            shutil.rmtree(dst)

        shutil.copytree(self.directory, dst)

        self.log_dir('install', self.directory, 'create exe script')
        link = r'''#!/bin/bash
%s/GoProVRPlayer.sh
''' % dst

        filename = os.path.join(self.prefix_dir, 'bin', 'goprovr')
        with open(filename, 'wt') as f:
            f.write(link)

        os.chmod(filename, stat.S_IRWXU | stat.S_IWGRP | stat.S_IXGRP)
