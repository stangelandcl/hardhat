from .base import GnuRecipe


class NodeJsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NodeJsRecipe, self).__init__(*args, **kwargs)
        self.name = 'nodejs'
        self.version = '7.10.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['c-ares']
        self.url = 'https://github.com/ggreer/the_silver_searcher/archive/' \
                   '$version.tar.gz'
