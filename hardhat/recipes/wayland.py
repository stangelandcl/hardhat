from .base import GnuRecipe


class WaylandRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WaylandRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'eb3fbebb8559d56a80ad3753ec3db800' \
                      'f587329067962dbf65e14488b4b7aeb0'
        self.name = 'wayland'
        self.version = '1.15.0'
        self.version_url = 'https://wayland.freedesktop.org/releases.html'
        self.depends = [
            'docbook-xml', 'docbook-xsl', 'dot',
            'doxygen', 'libffi', 'libpng', 'libxslt',
            'xmlto']
        self.url = 'http://wayland.freedesktop.org/releases/' \
                   'wayland-$version.tar.xz'

        # documentation depends on graphviz which depends on mesa
        # which depends on wayland. Circular dependency.
        # use the minimal graphviz project 'dot' instead
        # dot is missing fonts
        self.configure_args += ['--disable-documentation']

        def rm(x):
            self.environment[x] = self.environment[x].replace('-DNDEBUG', '')
        rm('CPPFLAGS')
        rm('CFLAGS')
        rm('CXXFLAGS')
