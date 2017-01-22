import os
from .base import GnuRecipe
from ..urls import Urls


class SbclRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SbclRecipe, self).__init__(*args, **kwargs)
        self.name = 'sbcl'
        self.version = '1.3.10'
        self.depends = ['texinfo']
        # Binary bootstrap
        self.sha256 = '387475206d173bccff8d7069d1295da6' \
                      '9b3ec341f96477538f29a3c119716593'

        self.url = Urls.sourceforge(
            'sbcl',
            'sbcl/%s/sbcl-%s-x86-64-linux-binary.tar.bz2'
            % (self.version, self.version))
        self.environment['INSTALL_ROOT'] = self.prefix_dir
        self.configure_args = self.shell_args + ['install.sh']

        # Source
        self.source_sha256 = '4a567aad91b316c22eb756dd8e502cfd' \
                             '9a95a4c660fb1fa2eb1e50e009b85777'
        self.source_url = Urls.sourceforge(
            'sbcl',
            'sbcl/%s/sbcl-%s-source.tar.bz2'
            % (self.version, self.version))
        self.compile_args = self.shell_args + [
            'make.sh', '--prefix=%s' % self.prefix_dir]
        self.install_args = self.shell_args + ['install.sh']
        self.environment['SBCL_HOME'] = '%s/lib/sbcl' % self.prefix_dir

    def configure(self):
        super(SbclRecipe, self).configure()

        self.sha256 = self.source_sha256
        self.url = self.source_url

        self.clean()
        self.download()
        self.extract()

    def compile(self):
        super(SbclRecipe, self).compile()

        # Make documentation
        dir = self.directory
        self.directory = os.path.join(dir, 'doc')
        self.compile_args = self.shell_args + ['make-doc.sh']
        super(SbclRecipe, self).compile()
        self.directory = dir
