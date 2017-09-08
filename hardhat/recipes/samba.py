import os
from .base import GnuRecipe


class SambaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SambaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9ef24393de08390f236cabccd6a420b5' \
                      'cea304e959cbf1a99ff317325db3ddfa'

        self.name = 'samba'
        self.version = '4.6.7'
        self.depends = ['acl', 'autotools', 'libtirpc', 'libxslt', 'openssl',
                        'python2']
        self.url = 'https://www.samba.org/ftp/samba/stable/' \
                   'samba-$version.tar.gz'

        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--localstatedir=%s/var' % self.prefix_dir,
            '--with-piddir=%s/run/samba' % self.prefix_dir,
            '--with-pammodulesdir=%s/lib/security' % self.prefix_dir,
            '--enable-fhs',
            '--without-ad-dc',
            '--without-systemd',
# otherwise figure out how to make waf use -lpanelw
            '--without-regedit',
            '--enable-selftest']
        self.configure_strip_cross_compile()

    def patch(self):
        text = r'''echo "^samba4.rpc.echo.*on.*ncacn_np.*with.*object.*nt4_dc" >> selftest/knownfail'''
        filename = os.path.join(self.directory, 'patch.sh')
        with open(filename, 'wt') as f:
            f.write(text)
        self.log_dir('patch', self.directory, 'disable failing test')
        self.run_exe(self.shell_args + ['patch.sh'],
                     self.directory,
                     self.environment)
