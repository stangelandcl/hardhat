from .base import GnuRecipe


class ItsToolRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ItsToolRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bf909fb59b11a646681a8534d5700fec' \
                      '99be83bb2c57badf8c1844512227033a'

        self.name = 'itstool'
        self.version = '2.0.2'
        self.depends = ['docbook-xml', 'libxml2', 'python2']
        self.url = 'http://files.itstool.org/itstool/itstool-$version.tar.bz2'
