from ..base import GnuRecipe


class OcamlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OcamlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '64ed6dad2316d5dff7440cea89f0f0ab' \
                      'e07ce508b9104d1bfadf3782e79856b4'

        self.name = 'ocaml'
        self.version = '4.04.0'
        self.depends = ['x11']
        self.url = 'http://caml.inria.fr/pub/distrib/ocaml-%s/' \
                   'ocaml-$version.tar.xz' % self.short_version

        self.configure_args = self.shell_args + [
            'configure',
            '-prefix',
            self.prefix_dir,
            '-fPIC']

        self.compile_args += ['world.opt']

    def need_configure(self):
        return True
