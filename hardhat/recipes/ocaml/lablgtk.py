from ..base import GnuRecipe


class LablGtkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LablGtkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2bf251db21c077fdd26c035ea03edd8f' \
                      'e609187f908e520e87a8ffdd9c36d233'
        self.name = 'lablgtk'
        self.version = '0.11.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://lablgtk.forge.ocamlcore.org/'
        self.depends = ['autotools', 'ocaml']
        self.url = 'https://forge.ocamlcore.org/frs/download.php/1627/' \
                   'lablgtk-$version.tar.gz'
