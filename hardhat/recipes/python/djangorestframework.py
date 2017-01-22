import os
from .base import SetupPyRecipe


class DjangoRestFrameworkRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(DjangoRestFrameworkRecipe, self).__init__(*args, **kwargs)

        self.name = 'djangorestframework'
        self.pydepends = ['django']
        self.version = '3.3.3'
        self.sha256 = 'f606f2bb4e9bb320937cb6ccce299991' \
                      'b2d302f5cc705a671dffca491e55935c'

    def patch(self):
        src = "return open(f, 'r').read()"
        dst = "return open(f, 'rt', encoding='utf-8').read()"
        filename = os.path.join(self.directory, 'setup.py')
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(src, dst)
        with open(filename, 'wt') as f:
            f.write(text)
