from ..base import GnuRecipe


class OcamlBuildRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OcamlBuildRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1717edc841c9b98072e410f1b0bc8b84' \
                      '444b4b35ed3b4949ce2bec17c60103ee'

        self.name = 'ocamlbuild'
        self.version = '0.11.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ocaml/ocamlbuild/releases'
        self.depends = ['autotools', 'ocaml']
        self.url = 'https://github.com/ocaml/ocamlbuild/archive/' \
                   '$version.tar.gz'
