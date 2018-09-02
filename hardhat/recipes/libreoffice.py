from .base import GnuRecipe


class LibreOfficeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibreOfficeRecipe, self).__init__(*args, **kwargs)
        self.name = 'libreoffice'
        self.version = '6.1.0.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = [
            'apr',
            'boost',
            'cups',
            'curl',
            'dbus-glib',
            'libjpeg-turbo',
            'glu',
            'graphite2',
            'gtk3',
            'harfbuzz',
            'icu',
            'java',
            'lcms',
            'librsvg',
            'libxml2',
            'libxslt',
            'mesa',
            'nss',
            'openldap',
            'openssl',
            'poppler',
            'postgres',
            'python3',
            'wget',
            'which',
            'unzip',
            'zip'
            ]
        self.url = 'http://downloadarchive.documentfoundation.org/libreoffice/old/$version/src/' \
                   'libreoffice-$version.tar.xz'
        self.compile_args = ['make', 'build-nocheck', '-j%s' % self.cpu_count]
        self.install_args = ['make', 'distro-pack-install']

    def configure(self):
        self.configure_args = [
            'sed', '-e', '"/gzip -f/d"', '-e', '"s|.1.gz|.1|g"',
            '-i', 'bin/distro-install-desktop-integration']
        super(LibreOfficeRecipe, self).configure()

        self.configure_args = [
            'sed', '-e', '"/distro-install-file-lists/d"', '-i', 'Makefile.in']
        super(LibreOfficeRecipe, self).configure()

        self.configure_args = ['./autogen.sh',
                               '--prefix=%s' % self.prefix_dir,
                               '--sysconfdir=%s/etc' % self.prefix_dir,
                               '--with-vendor=hardhat',
                               "--with-lang='fr en-GB'",
                               '--with-help',
                               '--with-myspell-dicts',
                               '--with-alloc=system',
                               '--without-junit',
                               '--without-system-dicts',
                               '--disable-dconf',
                               '--disable-odk',
                               '--disable-firebird-sdbc',
                               '--enable-release-build=yes',
                               '--enable-python=system',
                               '--with-system-apr',
                               '--with-system-boost',
                               '--with-system-cairo',
                               '--with-system-curl',
                               '--with-system-expat',
                               '--with-system-graphite',
                               '--with-system-harfbuzz',
                               '--with-system-icu',
                               '--with-system-jpeg',
                               '--with-system-lcms2',
                               '--with-system-libpng',
                               '--with-system-libxml',
                               '--with-system-nss',
                               '--with-system-odbc',
                               '--with-system-openldap',
                               '--with-system-openssl',
                               '--with-system-poppler',
                               '--with-system-postgresql',
                               '--with-system-zlib']
        super(LibreOfficeRecipe, self).configure()
