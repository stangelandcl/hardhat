from .base import GnuRecipe


class OpenMPIRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OpenMPIRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fed74f4ae619b7ebcc18150bb5bdb65e' \
                      '273e14a8c094e78a3fea0df59b9ff8ff'

        self.name = 'openmpi'
        self.version = '2.0.1'
        self.url = 'https://www.open-mpi.org/software/ompi/v%s/downloads/' \
                   'openmpi-$version.tar.bz2' % self.short_version
        self.configure_strip_cross_compile()
        self.environment_strip_lto()
