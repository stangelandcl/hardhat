from .base import GnuRecipe


class Extra:
    def __init__(self, name):
        self.name = name
        self.sha256 = None


class SwiPrologRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwiPrologRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7f17257da334bc1e7a35e9cf5cb8fca0' \
                      '1d82f1ea406c7ace76e9062af8f0df8b'

        self.name = 'swi-prolog'
        self.version = '7.4.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'http://www.swi-prolog.org/download/stable/src/' \
                   'swipl-$version.tar.gz'

        self.doc = Extra('swi-prolog-manual')
        self.doc.url = 'http://www.swi-prolog.org/download/stable/doc/' \
                       'SWI-Prolog-$version.pdf'

        self.configure_strip_cross_compile()

    def install(self):
        super(SwiPrologRecipe, self).install()

        self.log_dir('install', self.directory, 'install manual')
        filename = os.path.join(self.prefix_dir, 'doc',
                                os.path.basename(self.doc.filename))
        shutil.copy2(self.doc.filename, filename)
