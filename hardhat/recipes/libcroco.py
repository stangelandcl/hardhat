from .base import GnuRecipe


class LibcrocoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibcrocoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '132b528a948586b0dfa05d7e9e059901' \
                      'bca5a3be675b6071a90a90b81ae5a056'
                
        self.name = 'libcroco'
        self.depends = ['glib', 'gtk-doc', 'libxml2']
        self.version = '0.6.11'
        self.url = 'https://download.gnome.org/sources/libcroco/0.6/' \
                   'libcroco-$version.tar.xz'
