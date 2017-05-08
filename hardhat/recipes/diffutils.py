import os
from .base import GnuRecipe
from ..urls import Urls


class DiffUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DiffUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dad398ccd5b9faca6b0ab219a036453f' \
                      '62a602a56203ac659b43e889bec35533'

        self.description = 'patch and diff'

        self.name = 'diffutils'
        self.version = '3.5'
        self.url = Urls.gnu_template(name=self.name,
                                     version=self.version,
                                     extension='tar.xz')

    def patch(self):
        self.log_dir('patch', self.directory, 'fix compile')
        script = r'''#!/bin/bash
sed -i 's:= @mkdir_p@:= /bin/mkdir -p:' po/Makefile.in.in
sed -i '233,237 s/max)/max) \\/' lib/intprops.h
'''
        filename = os.path.join(self.directory, 'patch.sh')
        with open(filename, 'wt') as f:
            f.write(script)
        args = self.shell_args + [filename]
        self.run_exe(args, self.directory, self.environment)
