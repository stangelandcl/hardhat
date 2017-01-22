from .base import GnuRecipe


class NcduRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NcduRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '820e4e4747a2a2ec7a2e9f06d2f5a353' \
                      '516362c22496a10a9834f871b877499a'

        self.description = 'console disk space viewer'
        self.name = 'ncdu'
        self.version = '1.12'
        self.url = 'https://dev.yorhel.nl/download/ncdu-$version.tar.gz'
        self.environment['LIBS'] += ' -ltinfow'
