from string import Template
from .base import GnuRecipe


class NinjaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NinjaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '86b8700c3d0880c2b44c2ff67ce42774' \
                      'aaf8c28cbf57725cb881569288c1c6f4'
        self.name = 'ninja'
        self.version = '1.8.2'
        self.depends = ['asciidoc', 'doxygen', 'python2', 're2c']
        self.url = 'https://github.com/ninja-build/ninja/archive/' \
                   'v$version.tar.gz'

        self.configure_args = ['python2', 'configure.py', '--bootstrap']
#        self.compile_args = 'emacs -Q --batch -f batch-byte-compile' \
#                            ' misc/ninja-mode.el'.split()

# script:
#install -vDm644 misc/ninja-mode.el \
#                $prefix/share/emacs/site-lisp/ninja-mode.el &&
#install -vDm644 misc/ninja-mode.elc \
#                $prefix/share/emacs/site-lisp/ninja-mode.elc &&

        script = Template(r''' install -vm755 ninja $prefix/bin/ &&
install -vDm644 misc/ninja.vim \
                $prefix/share/vim/vim74/syntax/ninja.vim &&
install -vDm644 misc/bash-completion \
                $prefix/share/bash-completion/completions/ninja &&
install -vDm644 misc/zsh-completion \
                $prefix/share/zsh/site-functions/_ninja &&
ninja manual &&
mkdir -p $prefix/share/doc/ninja-$version &&
install -vm644 doc/manual.html \
               $prefix/share/doc/ninja-$version/manual.html
''').substitute(prefix=self.prefix_dir,
                version=self.version)
        self.install_args = [script]

    def compile(self):
        pass
