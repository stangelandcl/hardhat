from .base import GnuRecipe


class OwlLispRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OwlLispRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '090ef90af5f11e7bf7751b67ca96d5ca' \
                      'd3b405391966a96a888db8adb9b69978'

        self.name = 'owl-lisp'
        self.version = '0.1.13'
        self.url = 'https://github.com/aoh/$name/archive/v$version.tar.gz'
        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
