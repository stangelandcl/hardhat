from .base import GnuRecipe


class AgRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cb416a0da7fe354a009c482ae709692e' \
                      'd567f8e7d2dad4d242e726dd7ca202f0'

        self.name = 'ag'
        self.version = '2.1.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ggreer/the_silver_searcher/' \
                           'releases'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/ggreer/the_silver_searcher/archive/' \
                   '$version.tar.gz'

    def configure(self):
        self.configure_args = ['autoreconf', '-i']
        super(AgRecipe, self).configure()

        self.configure_args = self.shell_args + [
            'configure',
            '--prefix=%s' % self.prefix_dir]
        super(AgRecipe, self).configure()
