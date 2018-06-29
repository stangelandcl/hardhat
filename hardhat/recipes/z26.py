from .base import GnuRecipe


class Z26Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Z26Recipe, self).__init__(*args, **kwargs)
        self.description = 'Atari VCS/2600 emulator'
        self.name = 'z26'
        self.version = '3.02.01'
        self.depends = ['mesa']
        self.version_regex = r'z26v(?P<version>\d+\.\d+\.\d+)\.zip'
        self.version_url = 'http://www.whimsey.com/z26/z26.html'
        self.url = 'http://www.whimsey.com/z26/z26v3.02.01s.zip'
