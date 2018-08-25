import os
from hardhat.util import load_recipes


directory = os.path.dirname(__file__)
exclusions = ['__init__.py',
              'base.py',
              'gcc_prereq.py',
              'gcc_gmp.py',
              'gcc_isl.py',
              'gcc_mpc.py',
              'gcc_mpfr.py']


def load(settings):
    recipes = load_recipes(directory, 'hardhat.recipes.cross', exclusions)

    dependencies = [
        ['cross-make'],
        ['cross-binutils', 'cross-make'],
        ['cross-gcc',
         'cross-binutils',
         'cross-gcc1',
         'cross-linux-headers',
         'cross-glibc',
         'cross-libstdc++',
         'cross-binutils2',
         'cross-gcc2'],
        ['cross-gcc1', 'cross-binutils'],
        ['cross-linux-headers', 'cross-gcc1'],
        ['cross-glibc', 'cross-linux-headers'],
        ['cross-libstdc++', 'cross-glibc'],
        ['cross-binutils2', 'cross-libstdc++'],
        ['cross-gcc2', 'cross-binutils2']
        ]

    return (recipes, dependencies)
