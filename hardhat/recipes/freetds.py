import os
import shutil
from .base import GnuRecipe


class Extra:
    def __init__(self):
        self.sha256 = None


class FreeTdsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeTdsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '14df22fc14bc78dfdee274a25467767a' \
                      '464959c924bd3223192a99f446eaefb3'

        self.name = 'freetds'
        self.version = 'a0a3b99a7f3fb748f9ec5924d2913e6e856f659b'
        self.depends = ['autotools', 'docbook-dsssl', 'gettext',
                        'git', 'openssl']
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
        self.environment['CFLAGS'] += ' -fPIC'  # for shared libs
        self.doc = Extra()
        self.doc.version = '12.5.1'
        self.doc.url = 'http://infocenter.sybase.com/help/topic/' \
                       'com.sybase.help.ocs_$version.dblib/pdf/dblib.pdf'
        self.doc.name = 'dblib.pdf'
        self.doc.sha256 = '55216b1e8f2292d3a843b51ac31b9bbe' \
                          '8c3defd3e1f917546dfca8c692e9082a'
        self.extra_downloads.append(self.doc)

    def install(self):
        super(FreeTdsRecipe, self).install()

        self.log_dir('install', self.directory, 'install docs')

        docdir = os.path.join(self.prefix_dir, 'share', 'doc', self.name)
        dst = os.path.join(docdir, 'dblib.pdf')
        shutil.copy2(self.doc.filename, dst)


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
