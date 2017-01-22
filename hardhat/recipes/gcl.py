from .base import GnuRecipe


class GCLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GCLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8eb8491bccafc49683599e92a30ba36d' \
                      'b0825dd4bb138a104cb662b9b0d090e8'

        self.description = 'Gnu Common Lisp implementation'
        self.name = 'gcl'
        self.version = '2.6.12'
        self.url = 'http://reflection.oss.ou.edu/gnu/gnu/gcl/' \
                   'gcl-$version.tar.gz'
        self.configure_strip_cross_compile()
