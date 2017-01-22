from ..base import GnuRecipe


class CamlP5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CamlP5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '8fa2a46a7030b1194862650cbb71ab52' \
                      'a10a0174890560a8b6edf236f8937414'

        self.name = 'ocaml-camlp5'
        self.version = '6.17'
        v = self.version.replace('.', '')
        self.url = 'https://github.com/camlp5/camlp5/archive/rel%s.tar.gz' % v

        self.configure_args = self.shell_args + [
            'configure',
            '-prefix',
            self.prefix_dir]

        self.compile_args += ['world.opt']

    def need_configure(self):
        return True
