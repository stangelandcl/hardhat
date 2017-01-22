import os
import shutil
from .base import GnuRecipe
from hardhat.util import patch


class VsftpdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VsftpdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9d4d2bf6e6e2884852ba4e69e157a2ce' \
                      'cd68c5a7635d66a3a8cf8d898c955ef7'

        self.name = 'vsftpd'
        self.version = '3.0.3'
        self.url = 'https://security.appspot.com/downloads/' \
                   '$name-$version.tar.gz'

        self.environment['LDFLAGS'] += ' -lssp'

    def patch(self):
        filename = os.path.join(self.directory, "vsf_findlibs.sh")
        self.log_dir('patch', filename, 'search in prefix directory')
        patch(filename, 'locate_library /',
              'locate_library %s/' % self.prefix_dir)

        filename = os.path.join(self.directory, 'Makefile')
        self.log_dir('patch', filename, 'add -lssp')
        patch(filename, '`./vsf_findlibs.sh`', '`./vsf_findlibs.sh` -lssp')

        filename = os.path.join(self.directory, 'Makefile')
        self.log_dir('patch', filename, 'install to prefix')
        patch(filename, '/usr/', '%s/' % self.prefix_dir)

        filename = os.path.join(self.directory, 'Makefile')
        self.log_dir('patch', filename, 'bin not sbin')
        patch(filename, '/sbin/', '/bin/')

        filename = os.path.join(self.directory, 'Makefile')
        self.log_dir('patch', filename, 'install to prefix')
        patch(filename, '/etc/', '%s/etc/' % self.prefix_dir)

        filename = os.path.join(self.directory, 'defs.h')
        self.log_dir('patch', filename, 'change vsftpd.conf directory')
        patch(filename, '/etc/vsftpd.conf',
              '%s/etc/vsftpd.conf' % self.prefix_dir)

        filename = os.path.join(self.directory, 'tunables.c')
        self.log_dir('patch', filename, 'change vsftpd.conf directory')
        patch(filename, '/var/log/xferlog',
              '%s/var/log/xferlog' % self.prefix_dir)
        patch(filename, '/var/log/vsftpd.log',
              '%s/var/log/vsftpd.log' % self.prefix_dir)


        filename = os.path.join(self.directory, 'vsftpd.conf')
        self.log_dir('patch', filename, 'run as launching user')
        with open(filename, 'rt') as f:
            text = f.read()
        text += 'run_as_launching_user=YES\n' \
                'ftp_data_port=2120\n' \
                'listen_port=2121\n' \
                'no_anon_password=YES\n'
        with open(filename, 'wt') as f:
            f.write(text)

    def install(self):
        super(VsftpdRecipe, self).install()

        src = os.path.join(self.directory, 'vsftpd.conf')
        dst = os.path.join(self.prefix_dir, 'etc', 'vsftpd.conf')
        self.log_dir('install', self.directory, 'copy %s to %s' % (src, dst))
        shutil.copy2(src, dst)
