from .base import GnuRecipe
from hardhat.urls import Urls


class M4Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(M4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ab2633921a5cd38e48797bf5521ad259' \
                      'bdc4b979078034a3b790d7fec5493fab'

        self.name = 'm4'
        self.version = '1.4.18'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.gz')
        self.environment_strip_lto()

    def patch(self):
        self.log_dir('patch', self.directory, 'patch for glibc 1.28')

        filename = os.path.join(self.directory, 'lib', 'stdio-impl.h')
        with open(filename, 'rt') as f:
            text = f.read()
        text += '\n#define _IO_IN_BACKUP 0x100\n'
        with open(filename, 'wt') as f:
            f.write(text)

        files = ['fpurge.c', 'fflush.c', 'fseeko.c', 'fpending.c', 'freading.c',
                 'freadahead.c']
        for file in files:
            filename = os.path.join(self.directory, 'lib', file)
            src = 'IO_ftrylockfile'
            dst = 'IO_EOF_SEEN'
            patch(filename, src, dst)
