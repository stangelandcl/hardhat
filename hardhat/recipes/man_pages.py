from .base import GnuRecipe


class ManPagesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ManPagesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a574a08e4a62a24dc639cb4ee3e7aa68' \
                      'e7cd8ef2c14a5d54b90d09ac137e809c'

        self.name = 'man-pages'
        self.version = '4.09'
        self.depends = ['man-db']
        self.url = 'https://www.kernel.org/pub/linux/docs/man-pages/' \
                   'man-pages-$version.tar.xz'

        self.install_args = ['make',
                             'install',
                             'DESTDIR=%s' % self.prefix_dir,
                             'prefix=""']

    def compile(self):
        pass
