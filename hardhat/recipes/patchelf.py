from .base import GnuRecipe


class PatchElfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PatchElfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cf0693e794229e19edcf2299427b5a35' \
                      '2e0f4d4f06f9d3856e30ddb0344d5ce8'

        self.name = 'patchelf'
        self.depneds = ['autotools']
        self.version = '0.9'
        self.url = 'https://github.com/NixOS/patchelf/archive/$version.tar.gz'

    def configure(self):
        args = self.configure_args[:]
        self.configure_args = self.shell_args + ['./bootstrap.sh']
        super(PatchElfRecipe, self).configure()

        self.configure_args = args
        super(PatchElfRecipe, self).configure()
