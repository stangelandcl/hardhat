import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import patch
from ..version import extension_regex


class DDDRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DDDRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3ad6cd67d7f4b1d6b2d38537261564a0d' \
                      '26aaed077bf25c51efc1474d0e8b65c'

        self.name = 'ddd'
        self.version = '3.3.12'
        self.version_regex = 'ddd\-(?P<version>\d+\.\d+\.\d+)' \
                             + extension_regex
        self.depends = ['motif', 'xorg-libs']
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_args += ['--with-readline',
                                '--with-termlib=tinfow']
        self.configure_strip_cross_compile()

    def patch(self):
        src = '#include <stdlib.h>'
        dst = '#include <stdlib.h>\n#include <stdio.h>'  # for EOF
        filename = os.path.join(self.directory, 'ddd', 'strclass.C')
        patch(filename, src, dst)
