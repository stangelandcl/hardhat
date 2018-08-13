from .base import GnuRecipe


class GStreamerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GStreamerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4bd6127299f3f29379046bbd58a526e6' \
                      '353b569e0e72f7b4df2ae70df6882e09'
        self.name = 'gstreamer'
        self.depends = ['glib']
        self.version = '1.14.2'
        self.url = 'http://gstreamer.freedesktop.org/src/gstreamer/' \
                   'gstreamer-$version.tar.xz'

        self.environment['LDFLAGS'] += ' -Wl,-rpath-link,%s/libs/gst/base/' \
                                       '.libs/' % self.directory
