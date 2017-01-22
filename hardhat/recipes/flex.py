import os
from .base import GnuRecipe
from ..urls import Urls, GithubUrl


class FlexRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlexRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '68b2742233e747c462f781462a2a1e29' \
                      '9dc6207401dac8f0bbb316f48565c2aa'

        self.name = 'flex'
        self.version = '2.6.3'
        self.version_url = 'https://github.com/westes/flex/releases'
        self.url = 'https://github.com/westes/flex/releases/download/v$version/flex-$version.tar.gz'
        self.depends = ['autotools', 'bison']

        # doxygen fails to compile to compile with flex 2.6.0
        # when flex is built with cross-compile flags
        self.configure_strip_cross_compile()

    def install(self):
        super(FlexRecipe, self).install()

        src = os.path.join(self.prefix_dir, 'bin', 'flex')
        dst = os.path.join(self.prefix_dir, 'bin', 'lex')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
