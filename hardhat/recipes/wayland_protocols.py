from .base import GnuRecipe


class WaylandProtocolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WaylandProtocolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6b1485951fdcd36a960c870c46f28b03' \
                      'a3e5121fb46246916333ed07f78c98c5'
        self.name = 'wayland-protocols'
        self.version = '1.16'
        self.version_url = 'https://wayland.freedesktop.org/releases.html'
        self.depends = ['wayland']
        self.url = 'https://wayland.freedesktop.org/releases/' \
                   'wayland-protocols-$version.tar.xz'
#        self.configure_args += [
#            '--with-noarch-pkgconfigdir=%s/lib/pkgconfig' % self.prefix_dir]
