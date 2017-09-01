import os
from .base import GnuRecipe


class FreeTdsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeTdsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '14df22fc14bc78dfdee274a25467767a' \
                      '464959c924bd3223192a99f446eaefb3'

        self.name = 'freetds'
        self.version = 'a0a3b99a7f3fb748f9ec5924d2913e6e856f659b'
        self.depends = ['autotools', 'docbook-dsssl', 'git', 'openssl']
        self.url = self.github_commit('FreeTDS')
        self.configure_args = [
            ['git', 'init'],
            ['autoreconf', '-i'],
            ['git', 'add', '-f', 'configure'],
            ['git', 'commit', '-am', 'init'],
            ['./configure', '--prefix=%s' % self.prefix_dir,
             '--disable-odbc', '--disable-server', '--disable-pool',
             '--with-openssl', '--with-tdsver=7.3']]
        self.compile_args = ['make', '-j1']

    def install(self):
        super(FreeTdsRecipe, self).install()

        self.log_dir('install', self.directory, 'install docs')

        docdir = os.path.join(self.prefix_dir, 'share', 'doc', self.name)
        docdir = os.path.join(docdir, 'userguide')
        args = [
            ['wget', '--recursive', '--page-requisites',
             '--html-extension', '--convert-links', '--domains',
             'freetds.org',
             '--no-parent', 'http://www.freetds.org/userguide/'],
            ['rm', '-rf', docdir],
            ['cp', '-R', 'www.freetds.org', docdir]]
        for arg_list in args:
            self.log_dir('install', self.directory, ' '.join(arg_list))
            try:
                self.run_exe(arg_list, self.directory, self.environment)
            except Exception:
                if arg_list[0] != 'wget':
                    raise
