from .base import GnuRecipe


class ISyncRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ISyncRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9197e27bfe77e3d8971f4fcb25ec37b' \
                      '2506827c4bc9439b72376caa091ce877'
        self.name = 'isync'
        self.version = '1.2.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://downloads.sourceforge.net/isync/files/' \
                   '$name-$version.tar.gz'
