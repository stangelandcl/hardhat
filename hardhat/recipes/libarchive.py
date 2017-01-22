from .base import GnuRecipe


class LibArchiveRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibArchiveRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '691c194ee132d1f0f7a42541f091db81' \
                      '1bc2e56f7107e9121be2bc8c04f1060f'

        self.name = 'libarchive'
        self.version = '3.2.2'
        self.depends = ['libxml2', 'lzo', 'nettle']
        self.url = 'http://www.libarchive.org/downloads/' \
                   'libarchive-$version.tar.gz'
