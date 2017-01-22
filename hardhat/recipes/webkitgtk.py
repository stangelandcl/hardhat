from .base import GnuRecipe


class WebKitGtkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WebKitGtkRecipe, self).__init__(*args, **kwargs)
        self.name = 'webkitgtk'
        self.version = '2.12.4'
        self.depends = ['cairo', 'cmake', 'gst-plugins-base', 'gtk2', 'gtk3',
                        'icu', 'libgudev', 'libsecret', 'libsoup', 'libwebp',
                        'mesa', 'ruby', 'sqlite', 'which']
        self.url = 'http://webkitgtk.org/releases/webkitgtk-$version.tar.xz'

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DPORT=GTK',
            '-DUSE_LIBHYPHEN=OFF',
            '-DENABLE_MINIBROWSER=ON',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-Wno-dev'
            ]
