from .base import GnuRecipe


class Python2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ccd67509dfe45ec92432b7131df69468' \
                      '586c51ba7940aa70705f69bb068ba6cb'
        self.name = 'python2'
        self.version = '96f502059717a692ca3abd968b26c5ea2918ad3a'
        self.depends = ['bdb', 'bzip2', 'cacert', 'expat', 'gdbm', 'ncurses',
                        'openssl', 'readline', 'sqlite3', 'zlib']
        self.url = self.github_commit('python', 'cpython')
        self.configure_args += [
            '--enable-shared',
#           '--enable-profiling',
            '--enable-loadable-sqlite-extensions',
            '--enable-ipv6',
            '--with-dbmliborder=bdb:gdbm:ndbm',
#           '--with-pymalloc',
            '--with-threads',
            '--with-ensurepip=install',
            'ac_cv_file__dev_ptmx=yes',
            'ac_cv_file__dev_ptc=no',

            # force cross-compile
            '_PYTHON_HOST_PLATFORM=%s' % (self.host_triplet),

# We are only fake cross compiling so tell python it can use
# the just built version of python instead of requiring an extra
# version
            "PYTHON_FOR_BUILD='env LD_LIBRARY_PATH=. ./$(BUILDPYTHON) -E'"
            ]

        self.compile_args += ['profile-opt']
#                              '_PYTHON_HOST_PLATFORM=%s' % (self.HOST),
#                              'HOST_GNU_TYPE=%s' % (self.HOST)
#                              ]

    @property
    def short_version(self):
        # for boost
        return '2.7'


class Python2TkRecipe(Python2Recipe):
    def __init__(self, *args, **kwargs):
        super(Python2TkRecipe, self).__init__(*args, **kwargs)
        self.name = 'python2-tk'
        self.depends += ['tk']
