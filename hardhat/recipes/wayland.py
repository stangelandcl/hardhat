from .base import GnuRecipe


class WaylandRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WaylandRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6b4135cba0188abcb7275513c72dede' \
                      '751d6194f6edc5b82183a3ba8b821ab1'

        self.name = 'wayland'	
        self.version = '1.12.0'
        self.depends = [
            'docbook-xml', 'docbook-xsl'
            'doxygen', 'libffi', 'libxslt',
            'xmlto']
        self.url = 'http://wayland.freedesktop.org/releases/' \
                   'wayland-$version.tar.xz'

	# documentation depends on graphviz which depends on mesa
        # which depends on wayland. Circular dependency
        self.configure_args += ['--disable-documentation']

        def rm(x):
            self.environment[x] = self.environment[x].replace('-DNDEBUG', '')
        rm('CPPFLAGS')
        rm('CFLAGS')
        rm('CXXFLAGS')
