from .base import GnuRecipe


class RxvtUnicodeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RxvtUnicodeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e94628e9bcfa0adb1115d83649f898d6' \
                      'edb4baced44f5d5b769c2eeb8b95addd'

        self.name = 'rxvt-unicode'
        self.version = '9.22'
        self.depends = ['gdk_pixbuf', 'xorg-libs']
        self.url = 'http://dist.schmorp.de/rxvt-unicode/Attic/' \
                   'rxvt-unicode-$version.tar.bz2'
        self.configure_args += ['--enable-everything',
                                '--enable-256-color',
                                '--enable-text-blink',
                                '--enable-fading',
                                '--enable-font-styles',
                                '--enable-mousewheel',
                                '--enable-perl',
                                '--enable-pixbuf',
                                '--enable-startup-notification'
                                '--enable-xft',
                                '--enable-unicode',
                                '--with-term=rxvt-256color']

