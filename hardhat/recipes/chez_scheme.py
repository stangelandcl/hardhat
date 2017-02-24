from .base import GnuRecipe


class ChezSchemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChezSchemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '14aa903878590a30bbcbebb1de8ec2cd' \
                      'c12bf3974c307f771ef3fcfda3aa25ba'

        self.name = 'chez-scheme'
        self.version = 'e5802671c91378a91c3404f62e0e452590a975b7'
        self.depends = ['zlib']
        self.url = self.github_commit('cisco', 'ChezScheme')
        self.configure_args = self.shell_args + [
            './configure',
            '--64',
            '--threads',
            '--installprefix=%s' % self.prefix_dir]
        self.environment['LDFLAGS'] += ' -ltinfow -lz'
