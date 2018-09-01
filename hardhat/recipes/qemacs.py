from .base import GnuRecipe


class QemacsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(QemacsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2ffba66a44783849282199acfcc08707' \
                      'debc7169394a8fd0902626222f27df94'
        self.name = 'qemacs'
        self.version = '0.3.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://bellard.org/qemacs/'
        self.url = 'https://bellard.org/qemacs/qemacs-$version.tar.gz'
        self.configure_args += ['--disable-xv']
        self.compile_args = ['make', '-j1']
