from .base import GnuRecipe


class GraphVizRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GraphVizRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '81aa238d9d4a010afa73a9d2a704fc32' \
                      '21c731e1e06577c2ab3496bdef67859e'

        self.name = 'graphviz'
        self.version = '2.38.0'
        self.depends = ['freeglut', 'fontconfig', 'freetype',
                        'gdk-pixbuf', 'libjpeg-turbo', 'libpng', 'librsvg',
                        'lua', 'pango', 'python2', 'r', 'swig', 'xorg-libs']
        self.url = 'http://pkgs.fedoraproject.org/repo/pkgs/graphviz/' \
                   'graphviz-$version.tar.gz/' \
                   '5b6a829b2ac94efcd5fa3c223ed6d3ae/graphviz-$version.tar.gz'
