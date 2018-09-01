from .base import GnuRecipe


class JoeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JoeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '495a0a61f26404070fe8a719d80406dc' \
                      '7f337623788e445b92a9f6de512ab9de'
        self.name = 'joe'
        self.version = '4.6'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'ncurses']
        self.url = 'https://downloads.sourceforge.net/joe-editor/' \
                   'joe-$version.tar.gz'
