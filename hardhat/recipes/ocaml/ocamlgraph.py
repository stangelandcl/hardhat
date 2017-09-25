from ..base import GnuRecipe


class OcamlGraphRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OcamlGraphRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'df06ca06d25231bb8e162d6b853177cb' \
                      '7fc1565c8f1ec99ca051727d46c985a0'

        self.depends = ['autotools', 'lablgtk',
                        'ocaml', 'ocaml-findlib']
        self.name = 'ocamlgraph'
        self.version = '1.8.7'
        self.url = 'http://ocamlgraph.lri.fr/download/' \
                   'ocamlgraph-$version.tar.gz'
        self.configure_strip_cross_compile()
        self.install_args = ['make', 'install-findlib']
