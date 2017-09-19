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
#            '--sysconfdir=%s/etc' % self.prefix_dir,
#            '--localstatedir=%s/var' % self.prefix_dir,
#            '--with-piddir=%s/run/samba' % self.prefix_dir,
            '--with-pammodulesdir=%s/lib/security' % self.prefix_dir,
#            '--enable-fhs', # adds /sambda subdirectories
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

    def install(self):
        super(SambaRecipe, self).install()

        pkgconfig = r'''
prefix=$HARDHAT_PREFIX
exec_prefix=${prefix}
libdir=${prefix}/lib
includedir=${prefix}/include

Name: libsmbclient
Description: SMB client with dependencies
Version: %s
Libs: -Wl,-rpath,$HARDHAT_PREFIX/lib -L${libdir} -lsmbclient \
		-lsamba-util \
		-llibsmb-samba4 \
		-lmsrpc3-samba4 \
		-llibcli-lsa3-samba4 \
		-lreplace-samba4 \
		-lsamba-security-samba4 \
		-lsmbconf \
		$HARDHAT_PREFIX/lib/private/libtalloc.so.2 \
		-lndr \
		-lsamba-debug-samba4 \
		$HARDHAT_PREFIX/lib/private/libtevent.so.0 \
		-lcli-smb-common-samba4 \
		-lgse-samba4 \
		-lutil-cmdline-samba4 \
		-lsamba-errors \
		-ltevent-util \
		-lndr-standard \
		-ldcerpc-samba-samba4 \
		-lsamba3-util-samba4 \
		-lsecrets3-samba4 \
		-ltime-basic-samba4 \
		-lgenrand-samba4 \
		-lsocket-blocking-samba4 \
		-lrt \
		-lasn1util-samba4 \
		-lcli-cldap-samba4 \
		-lcliauth-samba4 \
		-lCHARSET3-samba4 \
		-lgensec-samba4 \
		$HARDHAT_PREFIX/lib/private/libcom_err-samba4.so.0 \
		-lndr-nbt \
		-lsamba-hostconfig \
		-lsmb-transport-samba4 \
		-lsamba-credentials \
		-lndr-samba-samba4 \
		-ldbwrap-samba4 \
		-ldcerpc-binding \
		-lutil-tdb-samba4 \
		-lsamba-sockets-samba4 \
		-lmessages-util-samba4 \
		-ltalloc-report-samba4 \
		-lmessages-dgm-samba4 \
		-lsmbd-shim-samba4 \
		-lserver-id-db-samba4 \
		-liov-buf-samba4 \
		-lsamba-cluster-support-samba4 \
		-lsys-rw-samba4 \
		-lutil-reg-samba4 \
		-linterfaces-samba4 \
		-lutil-setid-samba4 \
		-ltdb-wrap-samba4 \
		$HARDHAT_PREFIX/lib/private/libtdb.so.1 \
		-lserver-role-samba4 \
		-lnsl \
		-lcap \
		-llber \
		-lldap \
		$HARDHAT_PREFIX/lib/private/libkrb5-samba4.so.26 \
		-laddns-samba4 \
		$HARDHAT_PREFIX/lib/private/libgssapi-samba4.so.2 \
		-lkrb5samba-samba4 \
		-lauthkrb5-samba4 \
		-lcli-nbt-samba4 \
		$HARDHAT_PREFIX/lib/private/libldb.so.1 \
		-lcli-ldap-common-samba4 \
		-lwbclient \
		-lsamba-modules-samba4 \
		-lsamdb \
		-lsamdb-common-samba4 \
		-lldbsamba-samba4 \
		-lz \
		-lmsghdr-samba4 \
		-lresolv \
		-lsasl2 \
		-lssl \
		-lcrypto \
		$HARDHAT_PREFIX/lib/private/libheimbase-samba4.so.1 \
		$HARDHAT_PREFIX/lib/private/libasn1-samba4.so.8 \
		$HARDHAT_PREFIX/lib/private/libhx509-samba4.so.5 \
		$HARDHAT_PREFIX/lib/private/libhcrypto-samba4.so.5 \
		$HARDHAT_PREFIX/lib/private/libroken-samba4.so.19 \
		$HARDHAT_PREFIX/lib/private/libwind-samba4.so.0 \
		-ldl \
		-lndr-krb5pac \
		-lauth-sam-reply-samba4 \
		-lgnutls \
		-lwinbind-client-samba4 \
		-lflag-mapping-samba4 \
		-lp11-kit \
		-lidn \
		-ltasn1 \
		-lnettle \
		-lhogweed \
		-lgmp \
		-lffi
Cflags: -I${includedir} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64
URL: http://www.samba.org/
'''.replace("$HARDHAT_PREFIX", self.prefix_dir) % self.version

        self.log_dir('install', self.directory, 'installing libsmbclient.pc')
        file = os.path.join(
            self.prefix_dir, 'lib', 'pkgconfig', 'libsmbclient.pc')
        with open(file, 'wt') as f:
            f.write(pkgconfig)
