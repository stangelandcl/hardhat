from .base import GnuRecipe


class AprRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AprRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7d03ed29c22a7152be45b8e504310637' \
                      '36df9e1daa1ddf93f6a547ba7a28f67a'

        self.name = 'apr'
        self.version = '1.5.2'
        self.url = 'http://archive.apache.org/dist/apr/$name-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet,
            '--with-installbuilddir=%s/build/apr-1' % self.prefix_dir]
