from .base import GnuRecipe
from .graphviz import GraphVizRecipe


class LibGdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibGdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8c302ccbf467faec732f0741a859eef4' \
                      'ecae22fea2d2ab87467be940842bde51'
        self.name = 'libgd'
        self.version = '2.2.5'
        self.version_url = 'https://github.com/libgd/libgd/releases'
        self.url = 'https://github.com/libgd/libgd/releases/download/' \
                   'gd-$version/libgd-$version.tar.xz'
