from .base import GnuRecipe


class GnuTLSRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnuTLSRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9b50e8a670d5e950425d96935c7ddd41' \
                      '5eb6f8079615a36df425f09a3143172e'
               
        self.name = 'gnutls'
        self.version = '3.4.17'
        self.url = 'http://ftp.heanet.ie/mirrors/ftp.gnupg.org/gcrypt/gnutls/' \
                   'v3.4/gnutls-%s.tar.xz' % (self.version)
