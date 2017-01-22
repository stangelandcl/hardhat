import os
from hardhat.util import load_recipes

directory = os.path.dirname(__file__)
exclusions = ['__init__.py',
              'gcc_prereq.py',
              'gcc_gmp.py',
              'gcc_isl.py',
              'gcc_mpc.py',
              'gcc_mpfr.py']


def load(settings):
    recipes = load_recipes(directory, 'hardhat.recipes.toolchain', exclusions)

    dependencies = [
        ['binutils2', 'gcc'],
        ['gcc', 'binutils'],
        ['binutils', 'glibc'],
        ['glibc', 'linux-headers'],
        ['linux-headers', 'cross-gcc2'],
        ['toolchain',
         'binutils2', 'gcc', 'binutils', 'glibc',
         'linux-headers', 'cross-gcc2']
    ]

    return (recipes, dependencies)
