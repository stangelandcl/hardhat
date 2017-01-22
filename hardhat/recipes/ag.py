from .base import GnuRecipe


class AgRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4cb73a4436fccf2c2cae91479a0167ba' \
                      'caa968a4deca28f3ff9d5abd98f01009'

        self.name = 'ag'
        self.version = '1.0.2'
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
