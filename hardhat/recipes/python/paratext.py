import os
from .base import SetupPyRecipe


class ParaTextRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(ParaTextRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6a3f17ccc8c8b6410f349a4d11c34d55' \
                      '35197e2c36e98ad49c0c0f03e44fe321'

        self.depends = ['swig']
        self.name = 'paratext'
        self.version = '97a949a648f4f057e2b8764a6d2bb9be35cbfddf'
        self.url = 'https://github.com/wiseio/paratext/archive/' \
                   '$version.tar.gz'

    def patch(self):
        self.directory = os.path.join(self.directory, 'python')
