from ..base import GnuRecipe


class OcamlReRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OcamlReRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '262554309d645f4126a2a2e21e3a798d' \
                      '250293264fda34d6271243cc6c16e576'

        self.name = 'ocaml-re'
        self.version = '1.4.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'ocaml', 'ocamlbuild']
        self.url = 'https://github.com/ocaml/ocaml-re/archive/' \
                   'ocaml-re-$version.tar.gz'
        self.configure_strip_cross_compile()
