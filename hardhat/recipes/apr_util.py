from .base import GnuRecipe


class AprUtilRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AprUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a6cf327189ca0df2fb9d5633d7326c46' \
                      '0fe2b61684745fd7963e79a6dd0dc82e'

        self.name = 'apr-util'
        self.version = '1.5.4'
        self.url = 'http://archive.apache.org/dist/apr/$name-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--with-crypto',
            '--with-apr=%s' % self.prefix_dir,
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet
            ]
