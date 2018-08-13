from .base import GnuRecipe


class ECLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ECLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '76a585c616e8fa83a6b7209325a309da' \
                      '5bc0ca68e0658f396f49955638111254'
        self.description = 'Embedable Common Lisp implementation'
        self.name = 'ecl'
        self.version = '16.1.3'
        self.url = 'https://common-lisp.net/project/ecl/static/files/' \
                   'release/ecl-$version.tgz'
        self.configure_strip_cross_compile()
