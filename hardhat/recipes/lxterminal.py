from .base import GnuRecipe


class LxTerminalRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LxTerminalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '174b0e99652f72acd7a98b6ff1b75eba' \
                      '1a9bf364996e6f118cccdaba0d282baf'
                
        self.name = 'lxterminal'
        self.version = '0.2.0'
        self.depends = ['libxslt', 'docbook-xml', 'docbook-xsl', 'vte28']
        self.url = 'http://downloads.sourceforge.net/lxde/' \
                   '$name-$version.tar.gz'
        self.configure_args += ['--enable-man']
