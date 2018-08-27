from string import Template
from .base import GnuRecipe


class NinjaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NinjaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2edda0a5421ace3cf428309211270772' \
                      'dd35a91af60c96f93f90df6bc41b16d9'
        self.name = 'ninja'
        self.version = '1.7.2'
        self.depends = ['asciidoc', 'doxygen', 'python2']
        self.url = 'https://github.com/ninja-build/ninja/archive/v$version.tar.gz'

        self.configure_args = ['python2', 'configure.py', '--bootstrap']
#        self.compile_args = 'emacs -Q --batch -f batch-byte-compile' \
#                            ' misc/ninja-mode.el'.split()
        script = Template(r''' install -vm755 ninja $prefix/bin/ &&
install -vDm644 misc/ninja.vim \
                $prefix/share/vim/vim74/syntax/ninja.vim &&
install -vDm644 misc/bash-completion \
                $prefix/share/bash-completion/completions/ninja &&
install -vDm644 misc/zsh-completion \
                $prefix/share/zsh/site-functions/_ninja &&
#install -vDm644 misc/ninja-mode.el \
#                $prefix/share/emacs/site-lisp/ninja-mode.el &&
#install -vDm644 misc/ninja-mode.elc \
#                $prefix/share/emacs/site-lisp/ninja-mode.elc &&
ninja manual &&
mkdir -p $prefix/share/doc/ninja-$version &&
install -vm644 doc/manual.html \
               $prefix/share/doc/ninja-$version/manual.html
''').substitute(prefix=self.prefix_dir,
                version=self.version)
        self.install_args = [script]
