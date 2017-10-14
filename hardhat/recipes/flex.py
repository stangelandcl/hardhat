import os
from .base import GnuRecipe


class FlexRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlexRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e87aae032bf07c26f85ac0ed3250998c' \
                      '37621d95f8bd748b31f15b33c45ee995'

        self.name = 'flex'
        self.version = '2.6.4'
        self.version_url = 'https://github.com/westes/flex/releases'
        self.url = 'https://github.com/westes/flex/releases/download/' \
            'v$version/flex-$version.tar.gz'
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
