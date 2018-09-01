from .base import GnuRecipe


class EnchantRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EnchantRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'abd8e915675cff54c0d4da5029d95c52' \
                      '8362266557c61c7149d53fa069b8076d'

        self.name = 'enchant'
        self.version = '2.2.3'
        self.depends = ['glib']
        self.version_regex = 'enchant\-(?P<version>\d+\.\d+\.\d+)\.tar'
        self.version_url = 'https://github.com/AbiWord/enchant/releases'
        self.url = 'https://github.com/AbiWord/enchant/releases/download/' \
                   'v$version/enchant-$version.tar.gz'
