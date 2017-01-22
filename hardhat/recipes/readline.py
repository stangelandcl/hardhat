import os
from .base import GnuRecipe
from ..urls import Urls
from hardhat.util import patch


class ReadlineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ReadlineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '750d437185286f40a369e1e4f4764eda' \
                      '932b9459b5ec9a731628393dd3d32334'

        self.name = 'readline'
        self.version = '7.0'
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_args += ['--with-curses',
                                'bash_cv_wcwidth_broken=no'
                                ]
#        self.environment['LIBS'] = '-Wl,--no-as-needed -lncursesw' \
#                                   ' -Wl,--as-needed -lrt'

        self.environment['LDFLAGS'] += ' -Wl,--no-as-needed -lncursesw' \
                                       ' -Wl,--as-needed'

    def patch(self):
        filename = os.path.join(self.directory, 'rltypedefs.h')
        src = '#ifdef __cplusplus'
        dst = '''#include <stdio.h>
#ifdef __cplusplus'''
        patch(filename, src, dst)
