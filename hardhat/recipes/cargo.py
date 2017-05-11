import os
from .base import GnuRecipe


class Extra:
    def __init__(self, name):
        self.name = name
        self.sha256 = None


class CargoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CargoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fc689ca7a09f1e6a1c31e69f0e2616a9' \
                      '3576a68e0e1d7f0ae4c0d3301ff21ff8'

        self.name = 'cargo'
        self.version = '0.17.0'
        self.depends = ['cmake', 'rust', 'tar']
        self.url = 'https://github.com/rust-lang/cargo/archive/$version.tar.gz'

        self.configure_args = self.shell_args + [
            './configure',
            '--prefix=%s' % self.prefix_dir,
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--docdir=%s/sharp/doc/cargo-%s' % (self.prefix_dir, self.version),
            '--cargo=./cargo-nightly*/cargo/bin/cargo']

        self.rust_installer = Extra('rust-installer')
        self.rust_installer.version = '20161004'
        self.rust_installer.sha256 = '4f799e84410216180690496cd140de00' \
                                     '8d576f3052f3ee211cbddad2addccf21'
        self.rust_installer.url = 'http://anduin.linuxfromscratch.org/BLFS/' \
                                  'rust/rust-installer-$version.tar.xz'
        self.bootstrap_cargo = Extra('bootstrap-cargo')
        self.bootstrap_cargo.version = '0.16.0'
        self.bootstrap_cargo.sha256 = '0655713cacab054e8e5a33e742081eeb' \
                                      'ec8531a8c77d28a4294e6496123e8ab1'
        self.bootstrap_cargo.url = 'https://static.rust-lang.org/dist/' \
            'cargo-$version-x86_64-unknown-linux-gnu.tar.gz'

        self.extra_downloads += [self.rust_installer, self.bootstrap_cargo]

    def extract(self):
        super(CargoRecipe, self).extract()

        self.log_dir('extract', self.directory, 'untar bootstrap files')

        text = r'''#!/bin/bash
pushd src/rust-installer
tar -xf %s  --strip-components=1
popd
tar -xf %s
''' % (self.rust_installer.filename, self.bootstrap_cargo.filename)

        script = os.path.join(self.directory, 'untar_bootstrap.sh')
        with open(script, 'wt') as f:
            f.write(text)

        args = self.shell_args + [script]
        self.run_exe(args, self.directory, self.environment)
