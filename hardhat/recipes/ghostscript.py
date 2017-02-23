import os
import shutil
from .base import GnuRecipe


class Extra:
    pass

class GhostScriptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GhostScriptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a2dec70ab32ee83a05b8e257dfe3f308' \
                      '2ebe3a3d6c0f4c141b3b50ed4bda1564'
                
        self.name = 'ghostscript'
        self.version = '9.20'
        self.simple_version = self.version.replace('.', '')
        self.depends = ['expat',
                        'fontconfig',
                        'freetype',
                        'gtk3',
                        'libjpeg-turbo',
                        'libpng',
                        'libtiff',
                        'lcms']
        self.url = 'https://github.com/ArtifexSoftware/ghostpdl-downloads/' \
                   'releases/download/gs%s/' \
                   'ghostpdl-$version.tar.gz' % self.simple_version
        self.configure_args += ['--enable-dynamic',
                                '--disable-compile-inits',
                                '--with-system-libtiff']
        self.compile_args = [self.compile_args,
                             ['make', 'so', '-j%s' % self.cpu_count]]

        self.install_args = [
            self.install_args,
            ['make', 'soinstall'],
            ['install', '-v', '-m644', 'base/*.h',
             '%s/include/ghostscript' % self.prefix_dir],
            ['ln', '-v', '-s', 'ghostscript', '%s/include/ps' % self.prefix_dir]
        ]
        self.fonts = Extra()
        self.fonts.url = 'http://downloads.sourceforge.net/gs-fonts/$name-$version.tar.gz'
        self.fonts.version = '8.11'
        self.fonts.name = 'ghostscript-fonts-std'
        self.fonts.sha256 = '0eb6f356119f2e49b2563210852e17f5' \
                            '7f9dcc5755f350a69a46a0d641a0c401'        

        self.extra_downloads.append(self.fonts)

    def install(self):
        super(GhostScriptRecipe, self).install()
        self.log_dir('install', self.directory, 'installing fonts')

        args = ['tar', '-xvf', self.fonts.filename, '-C',
                '%s/share/ghostscript' % self.prefix_dir, '--no-same-owner']
        self.run_exe(args, self.directory, self.environment)

        args = ['fc-cache', '-v', '%s/share/ghostscript/fonts/' % self.prefix_dir]
        self.run_exe(args, self.directory, self.environment)

#    def patch(self):
#        self.log_dir('patch', self.directory, 'removing bundled libs')
#        shutil.rmtree(os.path.join(self.directory, 'freetype'))
#        shutil.rmtree(os.path.join(self.directory, 'lcms2'))
#        shutil.rmtree(os.path.join(self.directory, 'jpeg'))
#        shutil.rmtree(os.path.join(self.directory, 'libpng'))
#        shutil.rmtree(os.path.join(self.directory, 'zlib'))
        
        r'''TODO: (From BLFS)
Optional

Cairo-1.12.16, Cups-1.7.5, Fontconfig-2.11.1 (required, if you are installing any suggested font), GTK+-2.24.24, libidn-1.29, libpaper-1.1.24+nmu3, Little CMS-1.19 (not used by default, nor if lcms2 is present or found), and X Window System

User Notes: http://wiki.linuxfromscratch.org/blfs/wiki/gs

Installation of Ghostscript

[Note] Note
The Ghostscript build system is not user-friendly. In order to use system copies of various graphics libraries, you must do it using unconventional methods.

GPL Ghostscript includes (old) copies of several libraries. Some of these seem to have been patched to fix known vulnerabilities, but others of these copies are less-well maintained. To ensure that any future fixes are applied throughout the whole system, it is recommended that you first install the released versions of these libraries and then configure GPL Ghostscript to link to them.

If you have installed these dependencies on your system, remove the copies of expat, freetype, lcms2, libjpeg, and libpng:

sed -i 's/ZLIBDIR=src/ZLIBDIR=$includedir/' configure.ac configure &&
rm -rf expat freetype lcms2 jpeg libpng
Compile Ghostscript:

rm -rf zlib &&
./configure --prefix=/usr --disable-compile-inits \
 --enable-dynamic --with-system-libtiff &&
make
[Note] Note
The shared library depends on GTK+-2.24.24. It is only used in external programs like ImageMagick-6.8.9-7.

To compile the shared library libgs.so, run the following additional command as an unprivileged user:

make so
This package does not come with a test suite. However, you may test the operation of the newly built gs program by issuing the following command (issue from an X Window System terminal):

bin/gs -Ilib -IResource/Init -dBATCH examples/tiger.eps
Now, as the root user:

make install
If you want the shared library too:

make soinstall &&
install -v -m644 base/*.h /usr/include/ghostscript &&
ln -v -s ghostscript /usr/include/ps
Now make the documentation accessible from the normal place:

ln -sfv ../ghostscript/9.14/doc /usr/share/doc/ghostscript-9.14
If you have downloaded any fonts, unpack them to /usr/share/ghostscript and ensure the ownerships of the files are root: root. Substitute <font-tarball> appropriately in the command below for the fonts you wish to install:

tar -xvf ../<font-tarball> -C /usr/share/ghostscript --no-same-owner &&
fc-cache -v /usr/share/ghostscript/fonts/
'''
