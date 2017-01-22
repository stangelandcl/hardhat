from .base import GnuRecipe


class NssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NssRecipe, self).__init__(*args, **kwargs)
        self.name = 'nss'
        self.depends = ['nspr']
        self.version = '3.28'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        s = self.version.replace('.', '_')
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/security/nss/' \
                   'releases/NSS_%s_RTM/src/nss-$version.tar.gz' % s
