import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import patch


class MidoriRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MidoriRecipe, self).__init__(*args, **kwargs)
        self.name = 'midori'
        self.version = '6.5.6'
        self.depends = ['ncurses', 'texinfo']
        self.url = Urls.gnu_template(self.name, self.version)
#        self.environment['LIBS'] = ' -ltinfow -lncursesw'
        self.configure_args += ['--with-curses=yes']
