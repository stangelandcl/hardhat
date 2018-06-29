from .base import GnuRecipe


class P11KitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(P11KitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '58bae22f19db1de1a1103e7ca4149eed' \
                      '6e303e727878c2cd5ea9e6fe445fd403'

        self.name = 'p11-kit'
        self.version = '0.23.12'
        self.version_url = 'https://github.com/p11-glue/p11-kit/releases/'
        self.url = 'https://github.com/p11-glue/p11-kit/releases/download/' \
                   '$version/p11-kit-$version.tar.gz'
