import os
from .base import GnuRecipe
from ..util import patch


class MitKerberosRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MitKerberosRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '437c8831ddd5fde2a993fef425dedb48' \
                      '468109bb3d3261ef838295045a89eb45'

        self.name = 'mit-kerberos'
        self.version = '1.15.1'
        self.version_url = 'http://web.mit.edu/kerberos/dist/krb5/'
        self.url = 'http://web.mit.edu/kerberos/dist/krb5/$short_version/' \
                   'krb5-$version.tar.gz'
        self.depends = ['e2fsprogs',  # for libcom_err
                        'openldap',
                        'ntp']

        self.configure_args += ['--with-system-et',
                                '--with-system-ss',
                                '--with-system-verto=no',
                                '--enable-dns-for-realm']
        self.configure_strip_cross_compile()
        self.environment['CFLAGS'] += \
            ' -Wno-error=maybe-uninitialized -Wno-unused-variable'
        self.environment['CXXFLAGS'] += \
            ' -Wno-error=maybe-uninitialized -Wno-unused-variable'

    def configure(self):
        self.log_dir('configure', self.directory, 'autoconf')
        args = ['autoconf']
        self.run_exe(args, self.directory, self.environment)

        self.log_dir('configure', self.directory,
                     'patching configure for gcc warnings')
        filename = os.path.join(self.directory, 'configure')
        src = 'error=uninitialized'
        dst = ''
        patch(filename, src, dst)

        super(MitKerberosRecipe, self).configure()

    def patch(self):
        self.directory = os.path.join(self.directory, 'src')
        args = self.shell_args + ['-c', r'''
sed -e "s@python2.5/Python.h@& python2.7/Python.h@g" \
    -e "s@-lpython2.5]@&,\n  AC_CHECK_LIB(python2.7,main,[PYTHON_LIB=-lpython2.7])@g" \
    -i configure.in
''']

        self.log_dir('patch', self.directory, 'python version fixup')
        self.run_exe(args, self.directory, self.environment)
