from .base import GnuRecipe


class GambitSchemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GambitSchemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd8e2affb144013cbe22d09cf9c4120c8' \
                      '1edd9f075473de3605198b69405d6509'

        self.name = 'gambit-scheme'
        self.description = "Gambit Scheme"
        self.version = '4.8.5'
        underscore_version = self.version.replace('.', '_')
        self.url = 'http://www.iro.umontreal.ca/~gambit/download/gambit/v%s/' \
                   'source/gambit-v%s-devel.tgz' % (
                       self.short_version, underscore_version)
