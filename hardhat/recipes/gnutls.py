from .base import GnuRecipe


class GnuTLSRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnuTLSRecipe, self).__init__(*args, **kwargs)
        self.name = 'gnutls'
        self.version = '3.4.17'
        self.url = 'http://ftp.heanet.ie/mirrors/ftp.gnupg.org/gcrypt/gnutls/' \
                   'v3.4/gnutls-%s.tar.xz' % (self.version)
