import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import patch


class GlobalRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GlobalRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '43c64711301c2caf40dc56d7b91dd03d' \
                      '2b882a31fa31812bf20de0c8fb2e717f'
        self.name = 'global'
        self.version = '6.6.2'
        self.depends = ['ncurses', 'texinfo']
        self.url = Urls.gnu_template(self.name, self.version)
#        self.environment['LIBS'] = ' -ltinfow -lncursesw'
        self.configure_args += ['--with-curses=%s' % self.prefix_dir]
        self.configure_strip_cross_compile()

    def patch(self):
        self.log_dir('patch', self.directory, 'fix curses')
        filename = os.path.join(self.directory, 'configure')
        src = '-lncurses'
        dst = '-ltinfow -lncursesw'
        patch(filename, src, dst)
        src = '-lcurses'
        dst = '-ltinfow -lncursesw'
        patch(filename, src, dst)
