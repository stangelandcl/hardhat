from .base import GnuRecipe


class LibArchiveRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibArchiveRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ed2dbd6954792b2c054ccf8ec4b330a5' \
                      '4b85904a80cef477a1c74643ddafa0ce'

        self.name = 'libarchive'
        self.version = '3.3.2'
        self.depends = ['libxml2', 'lzo', 'nettle']
        self.url = 'http://www.libarchive.org/downloads/' \
                   'libarchive-$version.tar.gz'
