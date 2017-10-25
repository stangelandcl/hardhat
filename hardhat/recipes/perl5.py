import os
import stat
from .base import GnuRecipe
from hardhat.util import open_file, patch


class Perl5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Perl5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e430c6e0e0d9017c3f72898850dea65' \
                      '7fa6b51909220a7bcf305a87f2475202'

        self.name = 'perl5'
        self.version = '5.24.0'
        # Even numbered releases only. Odd numbers are development
        self.version_regex = r'perl\-(?P<version>\d+\.\d*[02468]\.\d+)\.tar\.gz'
        self.url = 'http://www.cpan.org/src/5.0/perl-$version.tar.gz'
        self.depends = ['bdb', 'gawk', 'gdbm', 'openssl']

        self.configure_args = self.shell_args + [
            './Configure',
            '-de',
            '-Dusethreads',
            '-Duselargefiles',
            '-Duseshrplib',
            '-Dcc=%s' % self.environment['CC'],
            '-Dprefix=%s' % self.prefix_dir]

        if self.use_root:
            self.configure_args += [
                '-Dlocincpth=%s/include' % self.prefix_dir,
                '-Dloclibpth="%s/lib %s/lib64"' % (
                    self.prefix_dir, self.prefix_dir),
                '-Aldflags=-Wl,-rpath,%s/lib,-rpath,%s/lib64'
                % (self.prefix_dir, self.prefix_dir),
            ]
        else:
            self.configure_args += [
                '-Dincpth=%s/include' % self.prefix_dir,
                '-Dlibpth=%s/lib' % self.prefix_dir,
                '-Aldflags=-R%s/lib' % self.prefix_dir,
    #            '-Dlibspth=%s/lib' % self.prefix_dir,
    #            '-Dglibpth=%s/lib' % self.prefix_dir,
    #            '-Dxlibpth=%s/lib' % self.prefix_dir,
    #            '-Dlocincpth=%s/include' % self.prefix_dir,
    #            '-Dloclibpth=%s/lib' % self.prefix_dir,

    #            '-Dusecrosscompile=yes',
    #            '-Dtargetarch=linux',
    #            '-Dtargethost=linux-x64',
    # cross-compiling to eliminate root directories
            ]
        self.environment['CFLAGS'] += ' -pthread'
        self.environment['LDFLAGS'] += ' -pthread'

    def patch(self):
        if self.use_root:
            return

        self.log_dir('patch', self.directory, 'patching many perl issues')
        text = """: change the next line if compiling for Xenix/286 on Xenix/386
xlibpth='/usr/lib/386 /lib/386'
: Possible local library directories to search.
loclibpth="/usr/local/lib /opt/local/lib /usr/gnu/lib"
loclibpth="$loclibpth /opt/gnu/lib /usr/GNU/lib /opt/GNU/lib"

: general looking path for locating libraries
glibpth="/lib /usr/lib $xlibpth"
glibpth="$glibpth /usr/ccs/lib /usr/ucblib /usr/local/lib"
test -f /usr/shlib/libc.so && glibpth="/usr/shlib $glibpth"
test -f /shlib/libc.so     && glibpth="/shlib $glibpth"
test -d /usr/lib64         && glibpth="$glibpth /lib64 /usr/lib64 /usr/local/lib64"
"""

        filename = os.path.join(self.directory, 'Configure')
        os.chmod(filename, stat.S_IRWXU)
        with open_file(filename, 'rt', encoding='utf-8') as f:
            text1 = f.read()
        text1 = text1.replace(text, '')

        text = '''locincpth="/usr/local/include /opt/local/include /usr/gnu/include"
    locincpth="$locincpth /opt/gnu/include /usr/GNU/include /opt/GNU/include"
    '''
        text1 = text1.replace(text, '')

        with open(filename, 'wt', encoding='utf-8') as f:
            f.write(text1)

#        src = """rp="Directories to use for library searches?"
#. ./myread
#case "$ans" in
#none) libpth=' ';;
#*) libpth="$ans";;
#esac"""

#        dst = 'echo libpth=$libpth'
#        patch(filename, src, dst)

        src = '''glibpth=`echo " $glibpth " | sed -e 's! /usr/shlib ! !'`
glibpth="/usr/shlib $glibpth"'''
        dst = ': skipping setting glibpth'
        patch(filename, src, dst)

        src = r'''    for var in xlibpth loclibpth locincpth glibpth; do
	eval xxx=\$$var
	eval $var=''
	for path in $xxx; do
	    eval $var=\"\$$var $sysroot$path\"
	done
    done
'''
        dst = "# Skipping setting lib paths with sysroot"
        patch(filename, src, dst)

        src = r'''libpth="`$echo $libpth|$sed 's/^ //'`"'''
        dst = r'''libpth="`$echo $libpth|$sed 's/^ //'`"
        # set plibpth to empty to remove sysroot directories
        plibpth=""
'''
        patch(filename, src, dst)


        # Disable LD_PRELOAD on linux. Causes problems the second
        # time perl is built
        # See http://www.nntp.perl.org/group/perl.perl5.porters/2015/12/
        #     msg233331.html
        src = 'linux)'
        dst = 'disable_linux1)'
        filename = os.path.join(self.directory, 'Makefile.SH')
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
        patch(filename, src, dst)
