from .base import GnuRecipe


class BlisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BlisRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c7efd75365a833614c01b5adfba9321' \
                      '0f869d92e7649e0b5d9edc93fc20ea76'

        self.description = 'modern C BLAS-like library includes BLAS API'
        self.name = 'blis'
        self.version = '0.4.0'
        self.version_url = 'https://github.com/flame/blis/releases'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+).\tar\.gz'
        self.url = 'https://github.com/flame/blis/archive/$version.tar.gz'
        self.configure_args = self.shell_args + [
            './configure', '-p', self.prefix_dir, 'haswell']
