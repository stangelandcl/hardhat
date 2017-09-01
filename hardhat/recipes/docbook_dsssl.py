import os
from .base import GnuRecipe


class DocbookDssslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DocbookDssslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2f329e120bee9ef42fbdd74ddd60e05e' \
                      '49786c5a7953a0ff4c680ae6bdf0e2bc'

        self.name = 'docbook-dsssl'
        self.version = '1.79'
        self.depends = ['sgml-common']
        self.url = 'https://downloads.sourceforge.net/docbook/' \
                   'docbook-dsssl-$version.tar.bz2'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        script = r'''
#!/bin/bash
install -v -m755 bin/collateindex.pl $prefix/bin
install -v -m644 bin/collateindex.pl.1 $prefix/share/man/man1
install -v -d -m755 $prefix/share/sgml/docbook/dsssl-stylesheets-1.79
cp -v -R * $prefix/share/sgml/docbook/dsssl-stylesheets-1.79

install-catalog --add $prefix/etc/sgml/dsssl-docbook-stylesheets.cat $prefix/share/sgml/docbook/dsssl-stylesheets-1.79/catalog

install-catalog --add $prefix/etc/sgml/dsssl-docbook-stylesheets.cat $prefix/share/sgml/docbook/dsssl-stylesheets-1.79/common/catalog

install-catalog --add $prefix/etc/sgml/sgml-docbook.cat $prefix/etc/sgml/dsssl-docbook-stylesheets.cat
'''.replace('$prefix', self.prefix_dir)

        file = os.path.join(self.directory, 'install.sh')
        with open(file, 'wt') as f:
            f.write(script)

        self.run_exe(self.shell_args + [file],
                     self.directory, self.environment)
