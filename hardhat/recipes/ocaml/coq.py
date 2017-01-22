from ..base import GnuRecipe


class CoqRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CoqRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6e3c3cf5c8e2b0b760dc52738e2e849f' \
                      '3a8c630869659ecc0cf41413fcee81df'
        self.name = 'coq'
        self.version = '8.6'
        self.depends = ['ocaml-findlib', 'ocaml-camlp5']
        self.url = 'https://coq.inria.fr/distrib/V$version/files/' \
                   'coq-$version.tar.gz'

        self.configure_args = self.shell_args + [
            'configure',
            '-prefix',
            self.prefix_dir]

    def need_configure(self):
        return True
