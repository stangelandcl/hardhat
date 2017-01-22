import os
from .base import GnuRecipe
from hardhat.urls import Urls


class NanoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NanoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b2b060129b9feff2d4870d803a441178' \
                      'c96531de9aed144ec0b83bd63ccb12ee'

        self.name = 'nano'
        self.version = '2.5.3'
        self.depends = ['ncurses']
        self.url = Urls.gnu(
            self.name,
            '$name-$version.tar.gz')

        self.configure_args += ['--enable-utf8',
                                'NCURSESW_LIBS="-ltinfo -lncursesw"']
        # --with-slang (if installed)

    def patch(self):
        dir = os.path.join(self.directory, 'doc', 'syntax')
        _, _, files = next(os.walk(dir))
        for filename in files:
            file = os.path.join(dir, filename)
            if file.endswith('.nanorc'):
                with open(file, 'rt', encoding='utf-8') as f:
                    text = f.read()
                text = text.replace('\\<', '\\b')
                text = text.replace('\\>', '\\b')
                with open(file, 'wt', encoding='utf-8') as f:
                    f.write(text)

    def install(self):
        super(NanoRecipe, self).install()

        nanorc = os.path.join(self.prefix_dir, 'etc', 'nanorc')
        with open(nanorc, 'wt') as f:
            f.write('include %s/share/nano/*\n' %
                    self.prefix_dir)
