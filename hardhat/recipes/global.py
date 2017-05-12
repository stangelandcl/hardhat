import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import patch


class GlobalRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GlobalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '122f9afa69a8daa0f64c12db7f02981f' \
                      'e573f51a163fa3829ed4f832cd281505'

        self.name = 'global'
        self.version = '6.5.6'
        self.depends = ['ncurses', 'texinfo']
        self.url = Urls.gnu_template(self.name, self.version)
#        self.environment['LIBS'] = ' -ltinfow -lncursesw'
        self.configure_args += ['--with-curses=yes']

    def patch(self):
        self.log_dir('patch', self.directory, 'fix curses')
        filename = os.path.join(self.directory, 'configure')
        src = '-lcurses'
        dst = '-ltinfow -lncursesw'
        patch(filename, src, dst)
