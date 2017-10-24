from .base import Mingw64BaseRecipe
from ..cacert import CACertRecipe


class Mingw64CurlRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64CurlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'de60a4725a3d461c70aa571d7d69c788' \
                      'f1816d9d1a8a2ef05f864ce8f01279df'

        self.name = 'mingw64-curl'
        self.version = '7.56.0'
        self.mingw64depends = ['zlib']
        self.url = 'https://curl.haxx.se/download/curl-$version.tar.bz2'
        self.configure_args += [
            '--enable-ldap',
            '--enable-ldaps',
            '--with-zlib',
            '--with-winssl'
            ]
