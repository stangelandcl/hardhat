from .base import SetupPyRecipe


class GuessRenamesRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(GuessRenamesRecipe, self).__init__(*args, **kwargs)

        self.sha256 = 'dfa69b31098ed9fe2ad87eb5d7e3c9ca' \
                      'a27ff9a4558488e5ceafad2f1acce64a'
        self.pythons = ['python2']
        self.name = 'guess-renames'
        self.version = '1453e85c1b0e3c6cf1b3da7c2ed588a375556944'
        self.url = 'https://github.com/stangelandcl/guess-renames/archive/' \
                   '$version.tar.gz'
