from ..base import GnuRecipe


class OpamRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpamRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '73367af7c127c1c865673d0369729dbe' \
                      '46d2d8d0d7a101f1d4a35135def58dfa'

        self.name = 'opam'
        self.version = '2.0.0-beta4'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ocaml/opam/' \
                           'releases'
        self.depends = ['autotools', 'ocaml', 'ocamlgraph', 'ocaml-re',
                        'opam-file-format']
        self.url = 'https://github.com/ocaml/opam/archive/$version.tar.gz'
        self.configure_strip_cross_compile()
