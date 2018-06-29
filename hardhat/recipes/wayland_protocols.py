from .base import GnuRecipe


class WaylandProtocolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WaylandProtocolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9648896b2462b49b15a69b60f4465659' \
                      '3c170c0e73121c890eb16d0c1d9376f6'

        self.name = 'wayland-protocols'
        self.version = '1.14'
        self.version_url = 'https://wayland.freedesktop.org/releases.html'
        self.depends = ['wayland']
        self.url = 'https://wayland.freedesktop.org/releases/' \
                   'wayland-protocols-$version.tar.xz'
#        self.configure_args += [
#            '--with-noarch-pkgconfigdir=%s/lib/pkgconfig' % self.prefix_dir]
