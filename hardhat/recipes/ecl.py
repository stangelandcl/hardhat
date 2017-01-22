from .base import GnuRecipe


class ECLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ECLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2d482b1a0a4fbd5d881434517032279d' \
                      '808cb6405e22dd91ef6d733534464b99'

        self.description = 'Embedable Common Lisp implementation'
        self.name = 'ecl'
        self.version = '16.1.2'
        self.url = 'https://common-lisp.net/project/ecl/static/files/' \
                   'release/ecl-$version.tgz'
        self.configure_strip_cross_compile()
