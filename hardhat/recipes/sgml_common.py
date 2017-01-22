import os
from .base import GnuRecipe


class SgmlCommonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SgmlCommonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7dc418c1d361123ffc5e45d61f1b9725' \
                      '7940a8eb35d0bfbbc493381cc5b1f959'

        self.name = 'sgml-common'
        self.version = '0.6.3'
        self.url = 'ftp://sources.redhat.com/pub/docbook-tools/new-trials/' \
                   'SOURCES/sgml-common-$version.tgz'

    def patch(self):
        file = os.path.join(self.directory, 'doc', 'man', 'Makefile.am')
        text = 'man_MANS = install-catalog.8'
        with open(file, 'wt') as f:
            f.write(text)

    def configure(self):
        args = self.configure_args
        self.configure_args = ['autoreconf', '-f', '-i']
        super(SgmlCommonRecipe, self).configure()
        self.configure_args = args
        super(SgmlCommonRecipe, self).configure()
