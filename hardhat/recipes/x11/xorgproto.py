import os
from ..base import GnuRecipe

class XOrgProtoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XOrgProtoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fee885e0512899ea5280c593fdb2735b' \
                      'eb1693ad170c22ebcc844470eec415a0'

        self.name = 'xorgproto'
        self.version = '2018.4'
        self.url = 'https://xorg.freedesktop.org/archive/individual/proto/' \
                   'xorgproto-$version.tar.bz2'

        self.depends = ['meson', 'ninja']
        self.install_args = ['cd', 'build', '&&', 'ninja', 'install']

    def configure(self):
        pass

    def compile(self):
        self.log_dir('compile', self.directory, 'build')
        script = os.path.join(self.directory, 'build.sh')
        text = r'''
mkdir build &&
cd    build &&

meson --prefix=$HARDHAT_PREFIX --datadir=$HARDHAT_PREFIX/lib .. &&
ninja
'''
        with open(script, 'wt') as f:
            f.write(text)

        args = self.shell_args + [script]
        self.run_exe(args, self.directory, self.environment)
