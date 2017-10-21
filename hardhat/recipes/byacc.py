from .base import GnuRecipe


class ByaccRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ByaccRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '27cf801985dc6082b8732522588a7b64' \
                      '377dd3df841d584ba6150bc86d78d9eb'

        self.name = 'byacc'
        self.version = '20170709'
        self.url = 'ftp://ftp.invisible-island.net/byacc/byacc-$version.tgz'
