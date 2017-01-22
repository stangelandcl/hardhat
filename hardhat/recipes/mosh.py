from .base import GnuRecipe


class MoshRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MoshRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1af809e5d747c333a852fbf7acdbf4d3' \
                      '54dc4bbc2839e3afe5cf798190074be3'

        self.name = 'mosh'
        self.version = '1.2.5'
        self.depends = ['protobuf']
        self.url = 'https://mosh.mit.edu/mosh-$version.tar.gz'
