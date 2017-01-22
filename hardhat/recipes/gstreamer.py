from .base import GnuRecipe


class GStreamerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GStreamerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '150e8e81febac94c161d8141cde78a38' \
                      '038a8f56e8ec549f353da54994278d65'

        self.name = 'gstreamer'
        self.depends = ['glib']
        self.version = '1.10.2'
        self.url = 'http://gstreamer.freedesktop.org/src/gstreamer/' \
                   'gstreamer-$version.tar.xz'

        self.environment['LDFLAGS'] += ' -Wl,-rpath-link,%s/libs/gst/base/' \
                                       '.libs/' % self.directory
