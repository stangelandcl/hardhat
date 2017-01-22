from .base import GnuRecipe


class ErlangRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ErlangRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fdab8129a1cb935db09f1832e3a7d511' \
                      'a4aeb2b9bb3602ca6a7ccb9730d5c9c3'

        self.name = 'erlang'
        self.version = '18.3'
        self.url = 'http://erlang.org/download/otp_src_$version.tar.gz'
        self.configure_strip_cross_compile()
