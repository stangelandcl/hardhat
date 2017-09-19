import os
import shutil
import stat
from .base import GnuRecipe


class GoProVRRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GoProVRRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8d5aa41ccfb4a6368f5816c958d0a59b' \
                      '2421394de440ffda620fafedb38886ff'
        self.name = 'goprovr'
        self.version = '231_2017-05-19'
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
