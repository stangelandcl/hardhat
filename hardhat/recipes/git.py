import os
from .base import GnuRecipe


class GitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8b40be383a603147ae29337136c00d1c' \
                      '634bdfdc169a30924a024596a7e30e92'

        self.name = 'git'
        self.version = '2.18.0'
        self.url = 'https://www.kernel.org/pub/software/scm/git/' \
                   'git-$version.tar.xz'

        self.depends = ['asciidoc',
                        'curl',
                        'docbook-xml',
                        'docbook-xsl',
                        'expat',
                        'openssl',
                        'pcre',
                        'perl',
                        'xmlto'
# Optional dependencies for GUI
                        #'python2',
                        #'tk'
                        ]
        gitconfig = os.path.join(self.prefix_dir, 'etc', 'gitconfig')
        self.configure_args += [
            '--with-gitconfig=%s' % gitconfig,
            '--with-libprce',
            '--with-curl',
            '--with-expat',
            '--with-openssl',
            '--with-perl=%s/bin/perl' % self.prefix_dir,
            'ac_cv_fread_reads_directories=yes',
            'ac_cv_snprintf_returns_bogus=no']
        self.environment['XMLTO'] = 'xmlto --skip-validation'

    def need_configure(self):
        return True

    def compile(self):
        super(GitRecipe, self).compile()

#        self.compile_args = ['make', 'html']
#        super(GitRecipe, self).compile()

        self.compile_args = ['make', 'man']
        super(GitRecipe, self).compile()

    def install(self):
        super(GitRecipe, self).install()

        self.install_args = ['make', 'install-man']
        super(GitRecipe, self).install()

#        self.install_args = ['make', 'install-html']
#        super(GitRecipe, self).install()
