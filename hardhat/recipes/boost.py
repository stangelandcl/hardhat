import os
from string import Template
from .base import GnuRecipe
from .python2 import Python2Recipe
from .python3 import Python3Recipe


class BoostRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BoostRecipe, self).__init__(*args, **kwargs)

        self.name = 'boost'
        self.version = '1.67.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)/'
        self.version_url = 'http://www.boost.org/users/download/'
        self.depends = ['bzip2', 'icu', 'openmpi',
                        'python2', 'python3', 'zlib']
        underscore_version = self.version.replace('.', '_')
        self.url = 'https://downloads.sourceforge.net/project/boost/boost/' \
                   '$version/boost_%s.tar.bz2' % (underscore_version)

        self.user_config = os.path.join(self.directory, 'user-config.jam')
        self.configure_args = self.shell_args + [
            '-c',
            '"./bootstrap.sh --prefix=%s"' % (self.prefix_dir)]

        self.install_args = self.shell_args + [
            '-c',
            '"./b2 install threading=multi'
            ' --without-python --user-config=%s -j%s"'
            % (self.user_config, self.cpu_count)
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'export config')
        python2 = Python2Recipe(settings=self)
        python3 = Python3Recipe(settings=self)
        self.python2_version = python2.short_version
        self.python3_version = python3.short_version

        extra_flags = '<compileflags>-Wno-unused-variable' \
                      ' <compileflags>-Wno-unused-local-typedefs'
        gcc = 'using gcc : : : %s ;\n' % extra_flags
        py3 = Template('using python : $version : '
                       '$prefix/bin/python$version :'
                       ' $prefix/include/python${version}m ;\n')
        py3 = py3.substitute(prefix=self.prefix_dir,
                             version=self.python3_version)
        py2 = Template('using python : $version : '
                       '$prefix/bin/python$version :'
                       ' $prefix/include/python${version} ;\n')
        py2 = py2.substitute(prefix=self.prefix_dir,
                             version=self.python2_version)
        mpi = 'using mpi ;'
        with open(self.user_config, 'wt') as f:
            f.write(gcc)
            f.write(py3)  # default version
            f.write(py2)
            f.write(mpi)
            f.write('\n')

    def compile(self):
        for version in [self.python2_version,
                        self.python3_version]:
            self.compile_args = self.shell_args + [
                '-c',
                '"./b2 install threading=multi'
                ' --with-python python=%s'
                ' --user-config=%s -j%s"'
                % (version, self.user_config, self.cpu_count)
                ]
            super(BoostRecipe, self).compile()
