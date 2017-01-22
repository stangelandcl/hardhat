from .base import GnuRecipe


class PolyMLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PolyMLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '20d7b98ae56fe030c64054dbe0644e9d' \
                      'c02bae781caa8994184ea65a94a0a615'

        self.name = 'polyml'
        self.version = '5.6'
        self.url = 'https://github.com/$name/$name/archive/v$version.tar.gz'
