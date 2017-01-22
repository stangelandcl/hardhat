import os
from .base import GnuRecipe


class FileRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2ef32b4ec936b0ff7b59a021dce56086' \
                      'a716663b6df1138c7ea597d396bf50cf'

        self.name = 'file'
        self.version = '5.26'
        self.url = 'ftp://ftp.astron.com/pub/file/file-$version.tar.gz'

        self.configure_strip_cross_compile()

#    def compile(self):
#        self.directory = os.path.join(self.directory, 'src')
#        super(FileRecipe, self).compile()
