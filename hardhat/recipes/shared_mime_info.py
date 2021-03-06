from .base import GnuRecipe


class SharedMimeInfoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SharedMimeInfoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c625a83b4838befc8cafcd54e3619946' \
                      '515d9e44d63d61c4adf7f5513ddfbebf'
        self.description = r'''very important for gtk2, gtk3, gdk-pixbuf
to be able to load icons. See https://trac.macports.org/ticket/45354 for
more info. If gtk3 fails to understand icon file types re-run the
update-mime-database $HARDHAT_PREFIX/share/mime code in the post_install
See https://forums.gentoo.org/viewtopic-t-798022-start-0.html
'''

        self.name = 'shared-mime-info'
        self.version = '1.10'
        self.depends = ['glib', 'libxml2']
        self.url = 'http://freedesktop.org/~hadess/' \
                   'shared-mime-info-$version.tar.xz'
        self.compile_args = ['make', '-j1']
