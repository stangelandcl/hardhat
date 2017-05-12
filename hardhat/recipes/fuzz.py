import os
import shutil
from .base import GnuRecipe
from hardhat.util import patch


class Extra:
        pass


class FuzzRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FuzzRecipe, self).__init__(*args, **kwargs)
        self.description = 'fuzz type-checker for Z by J.M. Spivey'
        self.sha256 = '3605480594f35678c7db151914ae2b59' \
                      'f06db86da1f692ff7212f43a96c5c470'
        self.name = 'fuzz'
        self.version = '3.4.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'http://spivey.oriel.ox.ac.uk/mike/fuzz/fuzz-$version.tgz'

        self.depends = ['flex', 'make', 'texlive']

        self.manual = Extra()
        self.manual.url = 'http://spivey.oriel.ox.ac.uk/mike/fuzz/fuzzman.pdf'
        self.manual.sha256 = '2ffe63543a57b6759179b661c121ef14' \
                             '1cd483a10801104d549a51a77d4c3469'
        self.manual.name = 'fuzz-fuzzman'
        self.manual.version = self.version

        self.reference = Extra()
        self.reference.url = 'http://spivey.oriel.ox.ac.uk/mike/fuzz/' \
                             'refcard.pdf'
        self.reference.sha256 = '274912fc9935597adcd576ef59f9412d' \
                                'b876ea5569dbfe4ada78346a485a578d'
        self.reference.name = 'fuzz-refcard'
        self.reference.version = self.version

        self.extra_downloads.append(self.manual)
        self.extra_downloads.append(self.reference)

        self.install_args += [
            'BINDIR=%s/bin' % self.prefix_dir,
            'LIBDIR=%s/lib' % self.prefix_dir,
            'TEXDIR=%s/texlive/texmf-local/tex' % self.prefix_dir,
            'MFDIR=%s/texlive/texmf-local/fonts/source/local' % self.prefix_dir
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'remove strncpy')
        text = 'EXTERN char *strncpy();'
        filename = os.path.join(self.directory, 'src', 'zscan.l')
        patch(filename, text, '')

        self.log_dir('patch', self.directory, 'fix fuzzlib path')
        src = "/usr/local/lib/fuzzlib"
        dst = "%s/lib/fuzzlib" % self.prefix_dir
        filename = os.path.join(self.directory, 'src', 'param.c')
        patch(filename, src, dst)

    def install(self):
        super(FuzzRecipe, self).install()

        dst = os.path.join(self.prefix_dir, 'share', 'doc', 'fuzz')
        if not os.path.exists(dst):
            os.makedirs(dst)
        shutil.copy2(self.manual.filename, os.path.join(dst, 'fuzzman.pdf'))
        shutil.copy2(self.reference.filename,
                     os.path.join(dst, 'Z-refcard.pdf'))
        shutil.copy2(os.path.join(self.directory, 'tex', 'tut.tex'),
                     os.path.join(dst, 'tut.tex'))
        shutil.copy2(os.path.join(self.directory, 'tex', 'example.tex'),
                     os.path.join(dst, 'example.tex'))

    def post_install(self):
        self.ldconfig()
        self.texhash()
