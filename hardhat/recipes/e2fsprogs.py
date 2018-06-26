import os
from .base import GnuRecipe


class E2FsProgsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(E2FsProgsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0ca164c1c87724df904c918b2d7051ef' \
                      '989b51de725db66c67514dbe6dd2b9ef'

        self.name = 'e2fsprogs'
        self.depends = ['tar']
#        self.depends = ['util-linux'] # fix circular dependencies
        self.version = '1.44.1'
        self.url = 'https://www.kernel.org/pub/linux/kernel/people/tytso/' \
                   'e2fsprogs/v$version/e2fsprogs-$version.tar.xz'
        self.configure_args += ['--enable-elf-shlibs',
                                '--enable-libblkid',
                                '--enable-libuuid',
                                '--disable-uuidd',
                                '--disable-fsck']
        self.install_args += ['install-libs']

    def extract(self):
        # extraction of version 1.44.1 fails in python with no linkname error
        cmd = 'tar xvf %s --directory %s && mv %s/* %s' % (
            self.filename,
            self.directory,
            os.path.join(self.directory, self.name + '-' + self.version),
            self.directory)
        self.log_dir('extract', self.directory, cmd)
        os.makedirs(self.directory)
        os.system(cmd)
