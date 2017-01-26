from .base import GnuRecipe
from .graphviz import GraphVizRecipe


class LibGdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '137f13a7eb93ce72e32ccd7cebdab687' \
                      '4f8cf7ddf31d3a455a68e016ecd9e4e6'

        self.name = 'libgd'
        self.version = '2.2.4'
        self.url = 'https://github.com/libgd/libgd/releases/download/gd-$version/libgd-$version.tar.xz'


