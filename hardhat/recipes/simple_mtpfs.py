import os
from .base import GnuRecipe


class SimpleMtpfsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SimpleMtpfsRecipe, self).__init__(*args, **kwargs)
        self.name = 'simple-mtpfs'
        self.version = '0.3.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'fuse', 'libmtp']
        self.configure_args += ['--with-tmpdir=%s/tmp' % self.prefix_dir]
        self.url = 'https://github.com/phatina/simple-mtpfs/archive/' \
                   'simple-mtpfs-$version.tar.gz'

    def install(self):
        super(SimpleMtpfsRecipe, self).install()

        self.log_dir('install', self.directory, 'write documentation')

        doc = r'''
From: https://wiki.archlinux.org/index.php/MTP
simple-mtpfs
List MTP devices:
$ simple-mtpfs -l
Your list of device(s) may look like this:
1: AsusZenfone 2 (MTP)
To mount the device with index 1 in the list to ~/mnt:
$ simple-mtpfs --device 1 ~/mnt
Unmount device mounted on ~/mnt:
$ fusermount -u ~/mnt
'''

        filename = os.path.join(self.prefix_dir, 'share', 'doc',
                                'simple-mtpfs', 'README')
        dir = os.path.dirname(filename)
        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(filename, 'wt') as f:
            f.write(doc)
