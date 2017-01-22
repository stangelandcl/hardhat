from .base import GnuRecipe


class TallocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TallocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '22d14911164d4de67ff76b5269fa5250' \
                      'd01f78c955bc77e28615350996877130'

        self.name = 'talloc'
        self.version = '2.1.8'
        self.depends = ['docboox-xml', 'docbook-xsl', 'libxslt', 'python3']
        self.url = 'https://www.samba.org/ftp/talloc/talloc-$version.tar.gz'
        self.configure_args += ['--extra-python=python3']
        self.configure_strip_cross_compile()
