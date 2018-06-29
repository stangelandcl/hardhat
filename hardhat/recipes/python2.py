from .base import GnuRecipe


class Python2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '616315d7f5939682ab1983d33afd7551' \
                      '0c6b6fcfcd779492b0e78debbedcaa95'

        self.name = 'python2'
        self.version = '468f97b4640e69b237a707a0ef9152d1c023f701'
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
