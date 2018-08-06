from .base import GnuRecipe


class AprUtilRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AprUtilRecipe, self).__init__(*args, **kwargs)
        self.name = 'apr-util'
        self.version = '1.6.1'
        self.url = 'http://archive.apache.org/dist/apr/$name-$version.tar.bz2'
        self.version_regex = 'apr\-util\-(?P<version>\d+\.\d+\.\d+)\.tar\.gz'

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--with-crypto',
            '--with-apr=%s' % self.prefix_dir,
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet
            ]
