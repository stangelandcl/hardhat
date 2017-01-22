from .base import GnuRecipe


class MotifRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MotifRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'afc5c93c03327a7207f5822c272aaf0d9' \
                      '8439007aa85a23149f833ba24916d25'

        self.name = 'motif'
        self.version = '2.3.5'
        self.depends = ['xorg-libs']
        self.url = 'https://sourceforge.net/projects/motif/files/' \
                   'Motif%202.3.5%20Source%20Code/motif-2.3.5.tar.gz/download'
        self.configure_strip_cross_compile()
        self.configure_args += ['--with-x']
        self.compile_args = ['make']
