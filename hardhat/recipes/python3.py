import os
from .base import GnuRecipe


class Python3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'aa472515800d25a3739833f76ca3735d' \
                      '9f4b2fe77c3cb21f69275e0cce30cb2b'

        self.name = 'python3'
        self.rebuilds = ['graphviz']
        self.depends = ['bdb', 'bzip2', 'cacert', 'expat', 'gdbm', 'ncurses',
                        'openssl', 'readline', 'sqlite3', 'xz', 'zlib']

        self.version = '3.6.0'
        self.url = \
            'https://www.python.org/ftp/python/$version/Python-$version.tgz'
        self.configure_args += [
            '--enable-shared',
#            '--enable-profiling',
            '--enable-loadable-sqlite-extensions',
            '--enable-ipv6',
            '--with-dbmliborder=bdb:gdbm:ndbm',
#                                '--with-pymalloc',
            '--with-threads',
            '--with-ensurepip=install',
            'ac_cv_file__dev_ptmx=yes',
            'ac_cv_file__dev_ptc=no',

            # force cross-compile
            '_PYTHON_HOST_PLATFORM=%s'
            % (self.host_triplet),

# Cross-compiling python requires a python >= 3.3. However it uses code from
# python 3.5. Since we are only fake cross compiling we can tell configure
# to use the just created python that it would use normally during a non-cross-
# compiled build.
            "PYTHON_FOR_BUILD='env LD_LIBRARY_PATH=. ./$(BUILDPYTHON) -E'"
                               ]

#        self.environment['CFLAGS'] = ''
#        self.environment['CXXFLAGS'] = ''
#        self.environment['CPPFLAGS'] = ''
#        self.environment['LDFLAGS'] = ''
#        self.environment['LIBS'] = ''
##        self.environment = {}

        self.compile_args += ['profile-opt']
#                              '_PYTHON_HOST_PLATFORM=%s' % (self.HOST),
#                              'HOST_GNU_TYPE=%s' % (self.HOST)
#                              ]

    def patch(self):
        config = os.path.join(self.directory, 'configure')
        with open(config, 'rt') as f:
            text = f.read()
        text = text.replace('(3,3)', '(3,5)')
        with open(config, 'wt') as f:
            f.write(text)


class Python3TkRecipe(Python3Recipe):
    def __init__(self, *args, **kwargs):
        super(Python3TkRecipe, self).__init__(*args, **kwargs)
        self.name = 'python3-tk'
        self.depends+= ['tk']
