from .base import GnuRecipe


class GraphVizRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GraphVizRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ca5218fade0204d59947126c38439f43' \
                      '2853543b0818d9d728c589dfe7f3a421'

        self.name = 'graphviz'
        self.version = '2.40.1'
        self.version_url = 'https://graphviz.gitlab.io/_pages/Download/' \
                           'Download_source.html'
        self.depends = ['freeglut', 'fontconfig', 'freetype',
                        'gdk-pixbuf', 'guile',
                        'java',
                        'libgd',
                        'libjpeg-turbo', 'libpng', 'librsvg',
                        'lua',
                        'ocaml', 'pango', 'python2', 'python3-tk', 'r',
                        'qt5', 'swig', 'tk', 'xorg-libs']
        self.url = 'https://graphviz.gitlab.io/pub/graphviz/stable/SOURCES/' \
                   'graphviz.tar.gz'
        self.configure_args += ['--with-libgd=no']
