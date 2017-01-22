import os
from .base import GnuRecipe
from ..urls import Urls


class PthRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PthRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '72353660c5a2caafd601b20e12e75d86' \
                      '5fd88f6cf1a088b306a3963f0bc77232'

        self.name = 'pth'
        self.version = '2.0.7'
        self.url = Urls.gnu_template(self.name, self.version)

    def patch(self):
        src = '$(LOBJS): Makefile'
        dst = '$(LOBJS): pth_p.h Makefile'

        filename = os.path.join(self.directory, 'Makefile.in')
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(src, dst)
        with open(filename, 'wt') as f:
            f.write(text)
