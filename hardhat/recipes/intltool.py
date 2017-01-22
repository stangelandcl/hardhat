from .base import GnuRecipe


class IntltoolRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IntltoolRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '67f25c5c6fb71d095793a7f895b245e6' \
                      '5e829e8bde68c6c8b4c912144ff34406'

        self.name = 'intltool'
        self.depends = ['perl5-xml-parser']
        self.version = '0.50.2'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://launchpad.net/intltool/trunk/$version/' \
                   '+download/intltool-$version.tar.gz'
