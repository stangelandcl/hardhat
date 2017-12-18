import os
import platform
import shutil
from hardhat.recipes.base import GnuRecipe
from hardhat.util import check_directory, patch
from hardhat.environment import target_path_env
from hardhat.recipes.cross.base import CrossGnuRecipe


class GLibCRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = self.glibc_sha256
        self.name = 'glibc'
        self.version = self.glibc_version
        self.url = 'http://ftp.wayne.edu/gnu/libc/glibc-%s.tar.gz' \
            % (self.version)

        self.directory = os.path.join(self.base_extract_dir,
                                      'glibc-%s-build' % (self.version))

        self.environment = target_path_env(self.prefix_dir,
                                           self.cross_prefix_dir)
        # enable debugging symbols so libpthread gets built with them
        # so gdb can debug threads.
        # According to http://lists.busybox.net/pipermail/buildroot/
        # 2012-September/058759.html
        # gdb searches for the debug symbol td_ta_new in libpthread and if not
        # found it won't go ahead and look for libthread_db
        self.environment['CFLAGS'] += ' -g'
        self.environment['CXXFLAGS'] += ' -g'


    def clean(self):
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)

    def patch(self):
        # _CS_PATH is used by execlp when PATH is null
        # PATH is null when execlp is called from a binary
        # that is setuid
        self.log_dir('patch', self.extract_dir, 'patch _CS_PATH')
        filename = os.path.join(self.extract_dir, 'sysdeps/unix/confstr.h')
        src = '"/bin:/usr/bin"'
        dst = '"%s/bin:%s/texlive/bin:%s/java/bin:/bin:/usr/bin"' % (
            self.prefix_dir, self.prefix_dir, self.prefix_dir)
        patch(filename, src, dst)

        # Intel can build with 2.6.32. Everything else needs 3.2.0 but the configure is
        # broken to always check for 3.2.0 which is wrong, so remove it
        self.log_dir('patch', self.extract_dir, 'remove minimum version check on intel')
        src = r'''
{ $as_echo "$as_me:${as_lineno-$LINENO}: checking installed Linux kernel header files" >&5
$as_echo_n "checking installed Linux kernel header files... " >&6; }
if ${libc_cv_linux320+:} false; then :
  $as_echo_n "(cached) " >&6
else
  cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
#include <linux/version.h>
#if !defined LINUX_VERSION_CODE || LINUX_VERSION_CODE <  (3 *65536+ 2 *256+ 0) /* 3.2.0 */
# error kernel headers missing or too old
#endif
int
main ()
{

  ;
  return 0;
}
_ACEOF
if ac_fn_c_try_compile "$LINENO"; then :
  libc_cv_linux320='3.2.0 or later'
else
  libc_cv_linux320='missing or too old!'
fi
rm -f core conftest.err conftest.$ac_objext conftest.$ac_ext
fi
{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $libc_cv_linux320" >&5
$as_echo "$libc_cv_linux320" >&6; }
if test "$libc_cv_linux320" != '3.2.0 or later'; then
  as_fn_error $? "GNU libc requires kernel header files from
Linux 3.2.0 or later to be installed before configuring.
The kernel header files are found usually in /usr/include/asm and
/usr/include/linux; make sure these directories use files from
Linux 3.2.0 or later.  This check uses <linux/version.h>, so
make sure that file was built correctly when installing the kernel header
files.  To use kernel headers not from /usr/include/linux, use the
configure option --with-headers." "$LINENO" 5
fi
'''
        filename = os.path.join(self.extract_dir, 'sysdeps/unix/sysv/linux/configure')
        patch(filename, src, '')


    def need_configure(self):
        return True

    def configure(self):
        check_directory(self.directory)
        super(GLibCRecipe, self).configure()

    def extract(self):
        super(GLibCRecipe, self).extract()

        prefix = os.path.join(self.prefix_dir, self.target_triplet)
        headers = os.path.join(self.prefix_dir, self.target_triplet, 'include')
        arch = platform.machine()

        # directory is not set until after extract
        self.configure_args = self.shell_args + [
            '%s/configure' % (self.extract_dir),
            '--prefix=%s' % (prefix),
            '--host=%s' % (self.target_triplet),
            '--target=%s' % (self.target_triplet),
#            '--build=%s' % (arch),
            '--with-headers=%s' % (headers),
            '--without-selinux',
            '--disable-multilib',
            '--enable-kernel=2.6.32',
            '--enable-obsolete-rpc',
        # for glibc 2.26:
        #
        # malloc.c:3572:25: error: array subscript is above array bounds [-Werror=array-bounds]
        # mfastbinptr *fb = &fastbin (av, idx);
        #
        # and more
            '--disable-werror'
#            'libc_cv_ssp=no',
#            'libc_cv_ssp_strong=no',
            ]

    def _replace(self, filename, src, dst):
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(src, dst)
        with open(filename, 'wt') as f:
            f.write(text)

    def post_install(self):
        # fix catchsegv libSegFault.so path
        target_base_dir = os.path.join(self.prefix_dir, self.target_triplet)
        file = os.path.join(target_base_dir, 'bin', 'catchsegv')
        self._replace(file, r'\$LIB', 'lib')


        # see here for emacs locale errors
        # http://unix.stackexchange.com/questions/195887/
        # emacs-text-mode-utf-8-characters
        dir = self.compile_directory()
        args = ['make',
                'localedata/install-locales'
                ]
        self.run_exe(args, dir, self.environment)


#        # update *.so paths to account for sysroot
#        lib_dir = os.path.join(target_base_dir, 'lib')
#        files = ['libc.so', 'libpthread.so', 'libm.so']
#
#        for file in files:
#            full = os.path.join(lib_dir, file)
#            self._replace(full, self.prefix_dir, '')




#        # The ldd scripts looks for ld-linux-x86-64.so.2 in the lib64
#        # directory. See: https://lists.gnu.org/archive/html/guix-devel/
#        # 2013-09/msg00138.html
#        # Or run sh -x ldd $(which ls) to see the paths it looks for
#        #
#        # Example dest path:
#        # $PREFIX/x86_64-srcinstall-linux-gnu/lib64/
#        # ld-linux-x86-64.so.2
#        ld_linux = 'ld-linux-x86-64.so.2'
#        src_file = os.path.join(target_base_dir, 'lib', ld_linux)
#        link_file = os.path.join(target_base_dir, 'lib64', ld_linux)
#        link_dir = os.path.dirname(link_file)
#        if not os.path.exists(link_dir):
#            os.makedirs(link_dir)
#        os.symlink(src_file, link_file)
