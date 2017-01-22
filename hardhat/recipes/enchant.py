from .base import GnuRecipe


class EnchantRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EnchantRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2fac9e7be7e9424b2c5570d8affe568d' \
                      'b39f7572c10ed48d4e13cddf03f7097f'

        self.name = 'enchant'
        self.version = '1.6.0'
        self.depends = ['glib']
        self.url = 'http://www.abisource.com/downloads/enchant/$version/' \
                   'enchant-$version.tar.gz'
