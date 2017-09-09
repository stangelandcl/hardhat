from .base import GnuRecipe
import os
from string import Template


class TexLiveRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TexLiveRecipe, self).__init__(*args, **kwargs)
        # No sha256 hash because file changes frequently
        # and there is no archive of old versions
        # and it is relatively small

        self.name = 'texlive'
        self.version = '3.14159265-2016'
        self.url = 'http://mirror.ctan.org/systems/texlive/tlnet/' \
                   'install-tl-unx.tar.gz'
        self.depends = ['perl5']
        self.profile_file = os.path.join(self.directory, 'texlive.profile')
        self.install_args = [
            'perl',
            'install-tl',
            '--profile=%s' % self.profile_file
        ]

#    def download(self):
        #rsync -a --delete rsync://somectan/somepath/systems/texlive/tlnet/ /your/local/dir

    def patch(self):
        PROFILE=r'''
# texlive.profile written on Sat Dec 17 00:11:29 2016 UTC
# It will NOT be updated and reflects only the
# installation profile at installation time.
selected_scheme scheme-full
TEXDIR ${prefix_dir}/texlive
TEXMFCONFIG ~/.texlive2016/texmf-config
TEXMFHOME ~/texmf
TEXMFLOCAL ${prefix_dir}/texlive/texmf-local
TEXMFSYSCONFIG ${prefix_dir}/texlive/texmf-config
TEXMFSYSVAR ${prefix_dir}/texlive/texmf-var
TEXMFVAR ~/.texlive2016/texmf-var
binary_x86_64-linux 1
collection-basic 1
collection-bibtexextra 1
collection-binextra 1
collection-context 1
collection-fontsextra 1
collection-fontsrecommended 1
collection-fontutils 1
collection-formatsextra 1
collection-games 1
collection-genericextra 1
collection-genericrecommended 1
collection-htmlxml 1
collection-humanities 1
collection-langarabic 1
collection-langchinese 1
collection-langcjk 1
collection-langcyrillic 1
collection-langczechslovak 1
collection-langenglish 1
collection-langeuropean 1
collection-langfrench 1
collection-langgerman 1
collection-langgreek 1
collection-langindic 1
collection-langitalian 1
collection-langjapanese 1
collection-langkorean 1
collection-langother 1
collection-langpolish 1
collection-langportuguese 1
collection-langspanish 1
collection-latex 1
collection-latexextra 1
collection-latexrecommended 1
collection-luatex 1
collection-mathscience 1
collection-metapost 1
collection-music 1
collection-omega 1
collection-pictures 1
collection-plainextra 1
collection-pstricks 1
collection-publishers 1
collection-texworks 1
collection-xetex 1
option_adjustrepo 1
option_autobackup 1
option_backupdir tlpkg/backups
option_desktop_integration 1
option_doc 0
option_file_assocs 1
option_fmt 1
option_letter 1
option_path 1
option_post_code 1
option_src 0
option_sys_bin ${prefix_dir}/bin
option_sys_info ${prefix_dir}/info
option_sys_man ${prefix_dir}/man
option_w32_multi_user 1
option_write18_restricted 1
portable 0
'''
        profile = Template(PROFILE).substitute(prefix_dir=self.prefix_dir)
        with open(self.profile_file, 'wt') as f:
            f.write(profile)


    def configure(self):
        pass

    def compile(self):
        pass
