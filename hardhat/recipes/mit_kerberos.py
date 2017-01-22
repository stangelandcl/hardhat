import os
from .base import GnuRecipe


class MitKerberosRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MitKerberosRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fd34752774c808ab4f6f864f935c4994' \
                      '5f5a56b62240b1ad4ab1af7b4ded127c'

        self.name = 'mit-kerberos'
        self.version = '1.15'
        self.version_url = 'http://web.mit.edu/kerberos/dist/krb5/'
        self.url = 'http://web.mit.edu/kerberos/dist/krb5/$version/' \
                   'krb5-$version.tar.gz'
        self.depends = ['e2fsprogs',  # for libcom_err
                        'openldap',
                        'ntp']

        self.configure_args += ['--with-system-et',
                                '--with-system-ss',
                                '--with-system-verto=no',
                                '--enable-dns-for-realm']
        self.configure_strip_cross_compile()

    def configure(self):
        self.log_dir('configure', self.directory, 'autoconf')
        args = ['autoconf']
        self.run_exe(args, self.directory, self.environment)
        super(MitKerberosRecipe, self).configure()

    def patch(self):
        patch = r'''From BLFS
Submitted By: Pierre Labastie <pierre dot labastie at neuf dot fr>
Date: 2017-01-20
Initial Package Version: 1.15
Upstream Status: Fixed in master
Origin: Upstream
Description: Fix starting daemons when the host is IPv4 only
See http://krbdev.mit.edu/rt/Ticket/display.html?id=8531

diff --git a/src/lib/apputils/net-server.c b/src/lib/apputils/net-server.c
index 171ecc404..d64ffddd6 100644
--- a/src/lib/apputils/net-server.c
+++ b/src/lib/apputils/net-server.c
@@ -834,7 +834,7 @@ setup_addresses(struct socksetup *data)
     };
     krb5_error_code ret = 0;
     size_t i;
-    int err;
+    int err, bound_any;
     struct bind_address addr;
     struct addrinfo hints, *ai_list = NULL, *ai = NULL;
     verto_callback vcb;
@@ -871,8 +871,12 @@ setup_addresses(struct socksetup *data)
          * Loop through all the sockets that getaddrinfo could find to match
          * the requested address.  For wildcard listeners, this should usually
          * have two results, one for each of IPv4 and IPv6, or one or the
-         * other, depending on the system.
+         * other, depending on the system.  On IPv4-only systems, getaddrinfo()
+         * may return both IPv4 and IPv6 addresses, but creating an IPv6 socket
+         * may give an EAFNOSUPPORT error, so tolerate that error as long as we
+         * can bind at least one socket.
          */
+        bound_any = 0;
         for (ai = ai_list; ai != NULL; ai = ai->ai_next) {
             /* Make sure getaddrinfo returned a socket with the same type that
              * was requested. */
@@ -889,9 +893,15 @@ setup_addresses(struct socksetup *data)
                                  _("Failed setting up a %s socket (for %s)"),
                                  bind_type_names[addr.type],
                                  paddr(ai->ai_addr));
-                goto cleanup;
+                if (ret != EAFNOSUPPORT)
+                    goto cleanup;
+            } else {
+                bound_any = 1;
             }
         }
+        if (!bound_any)
+            goto cleanup;
+        ret = 0;

         if (ai_list != NULL)
             freeaddrinfo(ai_list);
'''
        self.apply_patch(self.directory, patch)

        self.directory = os.path.join(self.directory, 'src')
        args = self.shell_args + ['-c', r'''
sed -e "s@python2.5/Python.h@& python2.7/Python.h@g" \
    -e "s@-lpython2.5]@&,\n  AC_CHECK_LIB(python2.7,main,[PYTHON_LIB=-lpython2.7])@g" \
    -i configure.in
''']

        self.log_dir('patch', self.directory, 'python version fixup')
        self.run_exe(args, self.directory, self.environment)
