from ..base import GnuRecipe


class OpamFileFormatRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpamFileFormatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '522773503b30ff755d04c4e11efb4657' \
                      'e21ac59499da270ef8040d88b4371b59'

        self.name = 'opam-file-format'
        self.version = '2.0.0-beta3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ocaml/opam-file-format/releases'
        self.depends = ['autotools', 'ocaml']
        self.url = 'https://github.com/ocaml/opam-file-format/archive/' \
                   '$version.tar.gz'
        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
