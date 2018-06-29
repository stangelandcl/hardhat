from .base import GnuRecipe


class AprRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AprRecipe, self).__init__(*args, **kwargs)
        self.name = 'apr'
        self.version = '1.6.3'
        self.url = 'http://archive.apache.org/dist/apr/$name-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet,
            '--with-installbuilddir=%s/build/apr-1' % self.prefix_dir]
