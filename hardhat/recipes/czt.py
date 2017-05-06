import os
import shutil
from .base import GnuRecipe
from ..urls import url_basename
from ..util import save_url


class CztRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CztRecipe, self).__init__(*args, **kwargs)
        self.name = 'czt'
        self.version = '1.0.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['texlive']

    def configure(self):
        pass

    def compile(self):
        pass

    def extract(self):
        pass

    def download(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing czt docs')
        urls = [
            'http://czt.sourceforge.net/latex/z/czt.sty',
            'http://czt.sourceforge.net/latex/circus/circus.sty',
            'http://czt.sourceforge.net/latex/z/czt-guide.pdf',
            'http://czt.sourceforge.net/latex/circus/circus-guide.pdf',
            'http://czt.sourceforge.net/latex/z/scheduler.tex',
            'http://czt.sourceforge.net/latex/z/scheduler.pdf',
            'http://czt.sourceforge.net/latex/circus/buffer-refinement-multienv.tex',
            'http://czt.sourceforge.net/latex/circus/buffer-refinement-multienv.pdf',
        ]

        doc_dir = os.path.join(self.prefix_dir, 'share', 'doc', 'czt')
        if not os.path.exists(doc_dir):
            os.makedirs(doc_dir)

        for url in urls:
            basename = url_basename(url)
            filename = os.path.join(doc_dir, basename)
            save_url(url, filename)
            if basename.endswith('.sty'):
                texdir = '%s/texlive/texmf-local/tex' % self.prefix_dir
                dst = os.path.join(texdir, 'czt.sty')
                shutil.copy2(filename, dst)
