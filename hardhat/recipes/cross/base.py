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
mpc_sha256 =  '617decc6ea09889fb08ede330917a00b' \
              '16809b8db88c29c31bfbb49cbf88ecc3'

isl_version = '0.16.1'  # recommended version for gcc
isl_sha256 = '412538bb65c799ac98e17e8cfcdacbb2' \
             '57a57362acfaaff254b0fcae970126d2'


class CrossGnuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGnuRecipe, self).__init__(*args, **kwargs)
        self.cross_prefix_dir = make_cross_prefix_dir(self.prefix_dir)
        self.environment = toolchain_env(self.cross_prefix_dir)

        self.gcc_version = '8.2.0'
        self.gcc_sha256 = '1b0f36be1045ff58cbb9c83743835367' \
                          'b860810f17f0195a4e093458b372020f'

        self.glibc_version = '2.28'
        self.glibc_sha256 = 'f318d6e3f1f4ed0b74d2832ac4f491d0' \
                            'fb928e451c9eda594cbf1c3bee7af47c'

        self.binutils_version = '2.31.1'
        self.binutils_sha256 = 'e88f8d36bd0a75d3765a4ad088d819e3' \
                               '5f8d7ac6288049780e2fefcad18dde88'
