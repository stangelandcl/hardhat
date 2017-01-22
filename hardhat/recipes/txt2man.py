from .base import GnuRecipe


class Txt2ManRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Txt2ManRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'df9d972c6930576328b779e64aed6d3e' \
                      '0106118e5a4069172f06db290f32586a'

        self.name = 'txt2man'
        self.version = '1.5.6'
        self.depends = ['gawk']
        self.url = 'https://github.com/mvertes/txt2man/archive/' \
                   'txt2man-$version.tar.gz'

        self.install_args = ['make', 'install', 'prefix=%s' % self.prefix_dir]

    def configure(self):
        pass

    def compile(self):
        pass
