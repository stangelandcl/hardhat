from .base import GnuRecipe


class Scheme48Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Scheme48Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c4921a90e95daee067cd2e9cc0ffe09' \
                      'e118f4da01c0c0198e577c4f47759df4'

        self.name = 'scheme48'
        self.version = '1.9.2'
        self.url = 'http://s48.org/$version/scheme48-$version.tgz'
        self.configure_strip_cross_compile()
