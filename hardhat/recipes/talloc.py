from .base import GnuRecipe


class TallocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TallocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b185602756a628bac507fa8af8b9df92' \
                      'ace69d27c0add5dab93190ad7c3367ce'
        self.name = 'talloc'
        self.version = '2.1.14'
        self.depends = ['docboox-xml', 'docbook-xsl', 'libxslt', 'python3']
        self.url = 'https://www.samba.org/ftp/talloc/talloc-$version.tar.gz'
        self.configure_args += ['--extra-python=python3']
        self.configure_strip_cross_compile()
