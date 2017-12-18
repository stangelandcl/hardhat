import datetime
import os
from hardhat.recipes.base import GnuRecipe
from hardhat.environment import toolchain_env


def make_cross_prefix_dir(prefix_dir):
    return os.path.join(prefix_dir, 'cross')


mpfr_version = '3.1.6'
mpfr_sha256 = 'cf4f4b2d80abb79e820e78c8077b6725' \
              'bbbb4e8f41896783c899087be0e94068'
gmp_version = '6.1.2'
gmp_sha256 = '5275bb04f4863a13516b2f39392ac5e2' \
            '72f5e1bb8057b18aec1c9b79d73d8fb2'
mpc_version = '1.0.3'
mpc_sha256 = '617decc6ea09889fb08ede330917a00b' \
             '16809b8db88c29c31bfbb49cbf88ecc3'
isl_version = '0.16.1'  # recommended version for gcc
isl_sha256 = '412538bb65c799ac98e17e8cfcdacbb2' \
             '57a57362acfaaff254b0fcae970126d2'


class CrossGnuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGnuRecipe, self).__init__(*args, **kwargs)
        self.cross_prefix_dir = make_cross_prefix_dir(self.prefix_dir)
        self.environment = toolchain_env(self.cross_prefix_dir)

        self.gcc_version = '7.2.0'
        self.gcc_sha256 = '0153a003d3b433459336a91610cca299' \
                          '5ee0fb3d71131bd72555f2231a6efcfc'

        self.glibc_version = '2.26'
        self.glibc_sha256 = 'dcc2482b00fdb1c316f385f8180e182b' \
                            'bd37c065dc7d8281a4339d2834ef1be7'

        self.binutils_version = '2.29'
        self.binutils_sha256 = '172e8c89472cf52712fd23a9f14e9bca' \
                               '6182727fb45b0f8f482652a83d5a11b4'
