import os
from .base import GnuRecipe


class DocbookXslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DocbookXslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '725f452e12b296956e8bfb876ccece71' \
                      'eeecdd14b94f667f3ed9091761a4a968'

        self.name = 'docbook-xsl'
        self.version = '1.79.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)/'
        self.version_url = 'https://sourceforge.net/projects/docbook/files/' \
                           'docbook-xsl/'
        self.depends = ['libxml2', 'libxslt']
        self.url = 'http://downloads.sourceforge.net/docbook/' \
                   'docbook-xsl-$version.tar.bz2'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        dir = '%s/share/xml/docbook/xsl-stylesheets-%s' \
              % (self.prefix_dir, self.version)
        self.install_args = ['install',
                             '-v',
                             '-m755',
                             '-d',
                             dir]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['cp',
                             '-v',
                             '-R',
                             'VERSION',
                             'assembly',
                             'common',
                             'eclipse',
                             'epub',
                             'epub3',
                             'extensions',
                             'fo',
                             'highlighting',
                             'html',
                             'htmlhelp',
                             'images',
                             'javahelp',
                             'lib',
                             'manpages',
                             'params',
                             'profiling',
                             'roundtrip',
                             'slides',
                             'template',
                             'tests',
                             'tools',
                             'webhelp',
                             'website',
                             'xhtml',
                             'xhtml-1_1',
                             'xhtml5',
                             dir]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['ln',
                             '-s',
                             '-f',
                             'VERSION',
                             '%s/VERSION.xsl' % dir]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['install',
                             '-v',
                             '-m644',
                             '-D',
                             'README',
                             '%s/README.txt' % dir]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['install',
                             '-v',
                             '-m644',
                             'RELEASE-NOTES*',
                             'NEWS*',
                             dir]
        super(DocbookXslRecipe, self).install()

        etc = '%s/etc/xml' % (self.prefix_dir)
        if not os.path.exists(etc):
            os.makedirs(etc)

        catalog = os.path.join(etc, 'catalog')
        if not os.path.exists(catalog):
            self.install_args = ['xmlcatalog',
                                 '--noout',
                                 '--create',
                                 catalog]
            super(DocbookXslRecipe, self).install()

        url = 'http://docbook.sourceforge.net/release/xsl/%s' % self.version
        self.install_args = ['xmlcatalog',
                             '--noout',
                             '--add',
                             '"rewriteSystem"',
                             url,
                             dir,
                             catalog]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['xmlcatalog',
                             '--noout',
                             '--add',
                             'rewriteURI',
                             url,
                             dir,
                             catalog]
        super(DocbookXslRecipe, self).install()

        url = 'http://docbook.sourceforge.net/release/xsl/current'
        self.install_args = ['xmlcatalog',
                             '--noout',
                             '--add',
                             'rewriteSystem',
                             url,
                             dir,
                             catalog]
        super(DocbookXslRecipe, self).install()

        self.install_args = ['xmlcatalog',
                             '--noout',
                             '--add',
                             'rewriteURI',
                             url,
                             dir,
                             catalog]
        super(DocbookXslRecipe, self).install()
