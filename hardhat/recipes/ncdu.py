from .base import GnuRecipe


class NcduRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NcduRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f4d9285c38292c2de05e444d0ba271cb' \
                      'fe1a705eee37c2b23ea7c448ab37255a'

        self.description = 'console disk space viewer'
        self.name = 'ncdu'
        self.version = '1.13'
        self.url = 'https://dev.yorhel.nl/download/ncdu-$version.tar.gz'
        self.environment['LIBS'] += ' -ltinfow'
