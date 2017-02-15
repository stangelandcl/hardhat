from .base import GnuRecipe


class LibKsbaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibKsbaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '41444fd7a6ff73a79ad9728f985e71c9' \
                      'ba8cd3e5e53358e70d5f066d35c1a340'
        self.name = 'libksba'
        self.version = '1.3.5'
        self.url = 'ftp://ftp.gnupg.org/gcrypt/$name/' \
            '$name-$version.tar.bz2'
