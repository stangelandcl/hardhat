import os
from .base import SetupPyRecipe


class PyTablesRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyTablesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '20fb453dcfbb28450f4f738ed8ce8594' \
                      '3b1cca4bf5e3cd739098cae6dac9dbc8'

        self.name = 'tables'
        self.version = '3.2.3.1'
        self.depends = ['bzip2', 'cython', 'hdf5', 'lzo']
        self.pydepends = ['numexpr', 'numpy']
        self.environment['LIBS'] = ''

    def compile(self):
        self.compile_args = [
            self.python,
            'setup.py',
            'build',
            '--hdf5=%s' % self.prefix_dir,
            '--bzip2=%s' % self.prefix_dir,
            '--lzo=%s' % self.prefix_dir,]
        super(SetupPyRecipe, self).compile()


    def install(self):
        self.install_args = [
            self.python,
            'setup.py',
            'install',
            '--force',
            '--hdf5=%s' % self.prefix_dir,
            '--bzip2=%s' % self.prefix_dir,
            '--lzo=%s' % self.prefix_dir,]
        super(SetupPyRecipe, self).install()
