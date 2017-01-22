from .base import GnuRecipe


class LuaJitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LuaJitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '620fa4eb12375021bef6e4f237cbd2dd' \
                      '5d49e56beb414bee052c746beef1807d'

        self.name = 'luajit'
        self.version = '2.0.4'
        self.url = 'http://luajit.org/download/LuaJIT-$version.tar.gz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]
