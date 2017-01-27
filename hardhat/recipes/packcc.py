import os
from .base import GnuRecipe
from ..urls import Urls
from ..util import read_url


class PackCCRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PackCCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b2fac154dfef862146b98a18a2daf74e' \
                      'c1042d4c2c29024217668bfe18cc549e'

        self.name = 'packcc'
        self.version = '1.2.0'
        self.url = Urls.sourceforge(
            'packcc',
            'packcc-%s/packcc-%s-linux-x64.tar.gz'
            % (self.version, self.version))

    def patch(self):
        makefile = '''
.PHONY: all

all:
\t${CC} ${CFLAGS} src/packcc.c -o bin/packcc
\tchmod +x bin/packcc
\tmkdir -p ${HARDHAT_PREFIX}/bin
\tcp bin/packcc ${HARDHAT_PREFIX}/bin
\tmkdir -p ${HARDHAT_PREFIX}/src
\tcp src/packcc.c ${HARDHAT_PREFIX}/src
\tmkdir -p ${HARDHAT_PREFIX}/doc
\tcp packcc.html ${HARDHAT_PREFIX}/doc
\tchmod +x bin/packcc-doc
\tcp bin/packcc-doc ${HARDHAT_PREFIX}/bin
install:
\techo 'nothing to do'
'''

        with open(os.path.join(self.directory, 'Makefile'), 'wt') as f:
            f.write(makefile)

        doc = r'''#!/bin/sh
firefox ${HARDHAT_PREFIX}/doc/packcc.html
'''
        with open(os.path.join(self.directory, 'bin', 'packcc-doc'), 'wt') as f:
            f.write(doc)

    def extract(self):
        super(PackCCRecipe, self).extract()
        self.log_dir('extract', self.directory, 'download docs')
        text = read_url('https://sourceforge.net/p/packcc/wiki/Home/')
        filename = os.path.join(self.directory, 'packcc.html')
        with open(filename, 'wb') as f:
            f.write(text)
