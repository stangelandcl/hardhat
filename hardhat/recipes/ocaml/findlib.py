from ..base import GnuRecipe


class FindLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FindLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5d4b9a79e9abf8be0b509f6b8cf56962' \
                      '21cbe14fa2fbb2bb352342755fd15eef'

        self.name = 'ocaml-findlib'
        self.version = '1.7.1'
        self.url = 'http://download.camlcity.org/download/' \
                   'findlib-$version.tar.gz'

        self.configure_args = self.shell_args + [
            'configure']

        # no parallel. it fails
        self.compile_args = ['make', 'all', 'opt']

    def need_configure(self):
        return True


