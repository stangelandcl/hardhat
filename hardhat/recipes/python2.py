from .base import GnuRecipe


class Python2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a4f05a0720ce0fd92626f0278b6b433e' \
                      'ee9a6173ddf2bced7957dfb599a5ece1'

        self.name = 'python2'
        self.version = '2.7.13'
        self.rebuilds = ['graphviz']
        self.depends = ['bdb', 'bzip2', 'cacert', 'expat', 'gdbm', 'ncurses',
                        'openssl', 'readline', 'sqlite3', 'zlib']
        self.url = \
            'https://www.python.org/ftp/python/%s/Python-%s.tgz' \
            % (self.version, self.version)
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
