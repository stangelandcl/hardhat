import os
from .base import GnuRecipe


class MercurialRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MercurialRecipe, self).__init__(*args, **kwargs)
        self.name = 'mercurial'
        self.version = '4.6.1'
        self.depends = ['guess-renames', 'hg-git', 'hg-zipdoc',
                        'python2-docutils']
        self.url = 'https://www.mercurial-scm.org/release/' \
                   'mercurial-$version.tar.gz'

        self.compile_args = [
            'make',
            'all',
            'DESTDIR=%s' % self.prefix_dir,
            'PREFIX=""'
            ]

        self.install_args = [
            'make',
            'install',
            'DESTDIR=%s' % self.prefix_dir,
            'PREFIX=""'
            ]

    def configure(self):
        pass

    def install(self):
        hgrc = """
[extensions]
guessrenames.hgext =
hggit =
zipdoc = %s/etc/mercurial/zipdoc.py

[encode]
**.docx = zipdocencode
**.odt = zipdocencode
**.pptx = zipdocencode

[decode]
**.docx = zipdocdecode
**.odt = zipdocdecode
**.pptx = zipdocdecode
"""

        file = os.path.join(self.prefix_dir, 'etc', 'mercurial', 'hgrc')
        dir = os.path.dirname(file)
        if not os.path.exists(dir):
            os.makedirs(dir)

        hgrc = hgrc % (self.prefix_dir)
        with open(file, 'wt') as f:
            f.write(hgrc)

        super(MercurialRecipe, self).install()
