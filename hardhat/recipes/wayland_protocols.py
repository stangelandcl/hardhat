from .base import GnuRecipe


class WaylandProtocolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WaylandProtocolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '635f2a937d318f1fecb97b54074ca211' \
                      '486e38af943868dd0fa82ea38d091c1f'

        self.name = 'wayland-protocols'
        self.version = '1.7'
        self.depends = ['wayland']
        self.url = 'https://wayland.freedesktop.org/releases/' \
                   'wayland-protocols-$version.tar.xz'
