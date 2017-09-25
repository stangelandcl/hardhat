from .base import GnuRecipe


class TisInterpreterRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TisInterpreterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'be28fe383822a2dab77d4399a5d1a80e' \
                      'bcf7fdcf92fe2355de8ff7bf25e957a2'
        self.description = 'C analyzer like valgrind'
        self.name = 'tis-interpreter'
        self.version = '33132ce4a825494ea48bf2dd6fd03a56b62cc5c3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'pkgconfig', 'ocaml-findlib',
                        'ocaml-graph']
        self.url = self.github_commit('TrustInSoft')
        self.configure_strip_cross_compile()
        self.compile_args = ['make', 'all', 'opt']
