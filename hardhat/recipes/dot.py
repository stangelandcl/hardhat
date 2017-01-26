from .base import GnuRecipe
from .graphviz import GraphVizRecipe


class DotRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DotRecipe, self).__init__(*args, **kwargs)
        self.name = 'dot'
        graphviz = GraphVizRecipe(settings=self)
        self.sha256 = graphviz.sha256
        self.version = graphviz.version
        self.url = graphviz.url

        self.documentation = 'graphviz without all the dependencies for' \
                             ' building documentation'
        self.configure_args += ['--without-x',
                                '--disable-swig',
                                '--without-glut']
