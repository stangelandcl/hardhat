import os
import shutil
import stat
from ..base import TarballRecipe


class SoftwareFoundationsRecipe(TarballRecipe):
    def __init__(self, *args, **kwargs):
        super(SoftwareFoundationsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '55376b75bcac244560b64b9c470422fa' \
                      '0bc6b53bf82c78eab71fabef054adfe1'

        self.name = 'software-foundations'
        self.version = '2016-05'
        self.url = 'https://www.cis.upenn.edu/~bcpierce/sf/current/sf.tgz'

    def configure(self):
        pass

    def install(self):
        dir = os.path.join(self.prefix_dir, 'doc', 'software-foundations')
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)
        SCRIPT=r'''#!/bin/bash

google-chrome %s/index.html

''' % dir

        script = os.path.join(self.prefix_dir, 'bin', 'software-foundations')
        with open(script, 'wt') as f:
            f.write(SCRIPT)
        os.chmod(script,
                 stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)
