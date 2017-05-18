from .base import GnuRecipe


class LibTorrentRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTorrentRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '44196a89932c26528f5db19289d0f0f4' \
                      '130730a61dccc61c9f1eac9ad3e881d8'
        self.name = 'libtorrent'
        self.version = '1.1.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        v = self.version.replace('.', '_')
        self.url = 'https://github.com/arvidn/libtorrent/releases/download/' \
                   'libtorrent-%s/libtorrent-rasterbar-$version.tar.gz' % v
