from .base import GnuRecipe


class CargoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CargoRecipe, self).__init__(*args, **kwargs)
        self.name = 'cargo'
        self.version = '0.17.0'
        self.depends = ['cmake', 'rust']
        self.url = 'https://github.com/rust-lang/cargo/archive/$version.tar.gz'

        self.compile_args = ['python2', './x.py', 'build']
        self.install_args = ['python2', './x.py', 'dist', '--install']
