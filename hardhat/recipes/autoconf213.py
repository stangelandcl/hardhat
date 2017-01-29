from .base import GnuRecipe
from ..urls import Urls


class AutoConf213Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AutoConf213Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f0611136bee505811e9ca11ca7ac188e' \
                      'f5323a8e2ef19cffd3edb3cf08fd791e'

        self.name = 'autoconf2.13'
        self.version = '2.13'
        self.url = Urls.gnu_template('autoconf', self.version)
        # install specific version for firefox
        self.configure_args += ['--program-suffix=2.13']
