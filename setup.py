#!/usr/bin/env python

import os
from setuptools import setup

filenames = [
    'setuptools-20.10.1.tar.gz',
    'argparse-1.4.0.tar.gz',
    'importlib-1.0.3.tar.gz'
]

filenames = list(filter(lambda x: os.path.exists(x), filenames))
filenames += ['bootstrap.sh']

with open('MANIFEST.in', 'wt') as f:
    for filename in filenames:
        f.write('include %s\n' % filename)

setup(name='hardhat',
      version='0.1',
      description='Python source based package manager',
      author='Clayton Stangeland',
      author_email='clayton.stangeland@gmail.com',
      url='xxx',
      packages=['hardhat',
                'hardhat.recipes',
                'hardhat.recipes.cross',
                'hardhat.recipes.doc',
                'hardhat.recipes.java',
                'hardhat.recipes.ocaml',
                'hardhat.recipes.perl',
                'hardhat.recipes.python',
                'hardhat.recipes.toolchain',
                'hardhat.recipes.x11'],
      package_data={'hardhat': ['scripts/symlinker.sh']},
      entry_points={
          'console_scripts': ['hardhat=hardhat.main:main']
          }
      )
