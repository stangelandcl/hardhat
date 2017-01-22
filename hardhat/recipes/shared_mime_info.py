from .base import GnuRecipe


class SharedMimeInfoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SharedMimeInfoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2af55ef1a0319805b74ab40d331a3962' \
                      'c905477d76c086f49e34dc96363589e9'

        self.name = 'shared-mime-info'
        self.version = '1.8'
        self.depends = ['glib', 'libxml2']
        self.url = 'http://freedesktop.org/~hadess/' \
                   'shared-mime-info-$version.tar.xz'
        self.compile_args = ['make', '-j1']
