from .base import GnuRecipe


class XapianRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XapianRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9783aeae4e1a6d06e5636b270db4b458' \
                      'a7d0804a31da158269f57fa5dc86347d'

        self.name = 'xapian'
        self.version = '1.2.23'
        self.url = 'http://oligarchy.co.uk/xapian/$version/' \
                   'xapian-core-$version.tar.xz'
