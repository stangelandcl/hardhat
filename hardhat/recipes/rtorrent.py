from .base import GnuRecipe


class RTorrentRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RTorrentRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ca89ca9e8f0cf984198d030203087e9' \
                      '3d24743dfa158091a5d225a70ca4c8cf'
                
        self.name = 'rtorrent'
        self.version = '0.9.6'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'curl', 'libtorrent']
        self.url = 'https://github.com/rakshasa/rtorrent/archive/$version.tar.gz'
        self.configure_args = [
            self.shell_args + ['./autogen.sh'],
            self.configure_args
            ]
