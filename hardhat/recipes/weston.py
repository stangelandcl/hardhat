from .base import GnuRecipe


class WestonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WestonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cbd3efbadacd14f3f9085166a863cbb7' \
                      '638fb01ad2b811db0b0f177212b6c2ef'

        self.name = 'weston'
        self.version = '5.0.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'wayland']
        self.url = 'https://github.com/wayland-project/weston/archive/$version.tar.gz'
        self.configure_args += ['--disable-xwayland-test']
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
        
