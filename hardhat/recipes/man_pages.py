from .base import GnuRecipe


class ManPagesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ManPagesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47ffcc0d27d50e497e290b27e8d76dbe' \
                      'd4550db14c881f25b771bcaf28354db4'
        self.name = 'man-pages'
        self.version = '4.16'
        self.depends = ['man-db']
        self.url = 'https://www.kernel.org/pub/linux/docs/man-pages/' \
                   'man-pages-$version.tar.xz'

        self.install_args = ['make',
                             'install',
                             'DESTDIR=%s' % self.prefix_dir,
                             'prefix=""']

    def compile(self):
        pass
