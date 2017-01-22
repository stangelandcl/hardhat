import os
from .base import PythonGnuRecipe
from hardhat.util import patch


class Python3PyCairoRecipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python3PyCairoRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.depends = ['cairo']
        self.name = 'pycairo'
        self.version = '1.10.0'
        self.url = 'https://www.cairographics.org/releases/' \
                   'pycairo-$version.tar.bz2'
        self.sha256 = '9aa4078e7eb5be583aeabbe8d8717279' \
                      '7717f95e8c4338f0d4a17b683a7253be'

    def run(self):
        self.clean()
        super(Python3PyCairoRecipe, self).run()

    def patch(self):
        self.environment['PYTHON'] = self.python
        self.configure_args = [self.python,
                               './waf',
                               'configure',
                               '--prefix=%s' % self.prefix_dir]

        self.compile_args = [self.python,
                             './waf',
                             'build']

        self.install_args = [self.python,
                             './waf',
                             'install',
                             '--force']

        self.log_dir('patch', self.directory, 'patching like Fedora 24')
        # Create .waf3-1.6.4-e3c1e08604b18a10567cfcd2d02eb6e6
        self.run_exe([self.python, 'waf', '--version'],
                     self.directory, self.environment)

        # waf decompresses itself here
        d = os.path.join(self.directory,
                         '.waf3-1.6.4-e3c1e08604b18a10567cfcd2d02eb6e6')

#        filename = os.path.join(d, 'waflib', 'Utils.py')
#        src = "f=open(fname,m)"
#        dst = "f = open(fname, m, encoding='utf-8')"
#        patch(filename, src, dst)

        filename = os.path.join(d, 'waflib', 'Tools', 'python.py')
        src = "for incstr in conf.cmd_and_log(conf.env.PYTHON+" \
              "[conf.env.PYTHON_CONFIG,'--includes']).strip().split():"
        dst = "for incstr in conf.cmd_and_log([conf.env.PYTHON_CONFIG," \
              "'--includes']).strip().split():"
        patch(filename, src, dst)

        filename = os.path.join(d, 'waflib', 'Build.py')
        src = "def store(self):"
        dst = "def store(self):\n\t\treturn"
        patch(filename, src, dst)


class Python2PyCairoRecipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Python2PyCairoRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python2']
        self.depends = ['cairo']
        self.name = 'pycairo'
        self.version = '1.10.0'
        self.url = 'https://cairographics.org/releases/' \
                   'py2cairo-$version.tar.bz2'
        self.sha256 = 'd30439f06c2ec1a39e27464c6c828b6e' \
                      'face3b22ee17b2de05dc409e429a7431'

    def run(self):
        self.clean()
        super(Python2PyCairoRecipe, self).run()

    def patch(self):
        self.environment['PYTHON'] = self.python
        self.configure_args = [self.python,
                               './waf',
                               'configure',
                               '--prefix=%s' % self.prefix_dir]

        self.compile_args = [self.python,
                             './waf',
                             'build']

        self.install_args = [self.python,
                             './waf',
                             'install',
                             '--force']

#        self.log_dir('patch', self.directory, 'patching like Fedora 24')
        # Create .waf3-1.6.4-e3c1e08604b18a10567cfcd2d02eb6e6
#        self.run_exe([self.python, 'waf', '--version'],
#                     self.directory, self.environment)

        # waf decompresses itself here
#        d = os.path.join(self.directory,
#                         '.waf3-1.6.4-e3c1e08604b18a10567cfcd2d02eb6e6')

#        filename = os.path.join(d, 'waflib', 'Utils.py')
#        src = "f=open(fname,m)"
#        dst = "f = open(fname, m, encoding='utf-8')"
#        patch(filename, src, dst)

#        filename = os.path.join(d, 'waflib', 'Tools', 'python.py')
#        src = "for incstr in conf.cmd_and_log(conf.env.PYTHON+" \
#              "[conf.env.PYTHON_CONFIG,'--includes']).strip().split():"
#        dst = "for incstr in conf.cmd_and_log([conf.env.PYTHON_CONFIG," \
#              "'--includes']).strip().split():"
#        patch(filename, src, dst)

#        filename = os.path.join(d, 'waflib', 'Build.py')
#        src = "def store(self):"
#        dst = "def store(self):\n\t\treturn"
#        patch(filename, src, dst)
