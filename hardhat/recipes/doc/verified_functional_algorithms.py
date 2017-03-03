import os
import shutil
import stat
from ..base import TarballRecipe


class VerifiedFunctionalAlgorithmsRecipe(TarballRecipe):
    def __init__(self, *args, **kwargs):
        super(VerifiedFunctionalAlgorithmsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b23d8375bc6138bbb7bea831d5d4a272' \
                      '13ed6334fb6663c36590cfced0adc001'
                
        self.name = 'verified-functional-algorithms'
        self.version = '2017-03'
        self.url = 'https://www.cs.princeton.edu/~appel/vfa/vfa.tgz'

    def configure(self):
        pass

    def install(self):
        dir = os.path.join(self.prefix_dir, 'doc', 'verified-functional-algorithms')
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)
        SCRIPT=r'''#!/bin/bash

firefox %s/index.html

''' % dir

        script = os.path.join(self.prefix_dir, 'bin', 'verified-functional-algorithms')
        with open(script, 'wt') as f:
            f.write(SCRIPT)
        os.chmod(script,
                 stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH | stat.S_IXOTH)


