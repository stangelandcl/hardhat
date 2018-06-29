import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import save_url


class BashRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BashRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '604d9eec5e4ed5fd2180ee44dd756ddc' \
                      'a92e0b6aa4217bbab2b6227380317f23'

        self.name = 'bash'
        self.version = '4.4.18'
        self.url = Urls.gnu_template(self.name, self.version)
        self.doc_url = 'https://www.gnu.org/software/bash/manual/bash.html'
        self.doc_file = os.path.join(self.prefix_dir, 'doc', 'bash.html')
        self.depends = ['bison', 'ncurses', 'readline']

        # Very important
        # If you don't strip cross-compiling then bash almost works but fails
        # in at least one case. On Fedora 23 x64 it will fail in this way:
        # 1. open an interactive session of new bash with ./bash in the bulid
        #    directory
        # 2. Run (cd doc && pwd) - with parentheses included so in a subshell
        # 3. Bash will print the home directory like it ignored the first
        #    argument 'doc'
        self.configure_strip_cross_compile()


        self.configure_args += ['--enable-directory-stack',
                                '--enable-history',
                                '--enable-multibyte',
                                '--with-installed-readline',
                                '--without-bash-malloc',
                                '--with-afs',
                                '--with-curses']
        self.compile_args += ['"CPPFLAGS=-D_GNU_SOURCE -DRECYCLE_PIDS"']

    def install(self):
        super(BashRecipe, self).install()
        src = os.path.join(self.prefix_dir, 'bin', 'bash')
        dst = os.path.join(self.prefix_dir, 'bin', 'sh')
        if os.path.lexists(dst):
            os.remove(dst)
        os.symlink(src, dst)

        self.log_dir('install', self.directory, 'installing html documentation')
        save_url(self.doc_url, self.doc_file)

    def post_install(self):
        test = '(cd doc && pwd)'
        result = os.path.join(self.directory, 'doc')
        # test that test==result when run from the new shell
