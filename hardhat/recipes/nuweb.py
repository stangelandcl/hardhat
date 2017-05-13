from .base import GnuRecipe


class NuWebRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NuWebRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fe909b703c707c04f778c3d3d2f1eed2' \
                      'e10034f7025d292dd9ae041feb88a160'

        self.name = 'nuweb'
        self.version = '1.58'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['texlive']
        self.url = 'http://downloads.sourceforge.net/nuweb/' \
                   'nuweb-$version.tar.gz'
        self.configure_args = [
            ['make', 'nuweb'],
            ['cp', 'nuweb', '%s/bin/nuweb' % self.prefix_dir],
            ['nuweb', 'nuwebsty.w']]
        self.compile_args = ['make', 'distribution']
        docs = '%s/share/doc/nuweb' % self.prefix_dir
        self.install_args = [
            ['mkdir', '-p', docs],
            ['cp', 'nuweb.pdf', docs],
            ['cp', 'nuwebdoc.pdf', docs],
            ['cp', 'nuwebdoc.tex', docs],
            ['cp', 'nuweb.tex', docs],
            ['cp', 'nuweb.w', docs],
            ['cp', '*.sty', '%s/texlive/texmf-local/tex' % self.prefix_dir]]

    def need_configure(self):
        return True
