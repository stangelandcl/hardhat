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


#https://www.reddit.com/r/urxvt/comments/3ep4u6/can_i_make_urxvt_pop_up_a_warning_or_something/
#I've had this exact problem! Now I always make a small tweak to the tabbed plugin to prevent closing down the whole urxvt window. With this change, I have to manually Ctrl-D each tab in turn to close it all down, which has worked great.
#Edit /usr/lib/urxvt/perl/tabbed and in the on_wm_delete_window function comment out the call to destroy (line 310 for me) with a #:
#sub on_wm_delete_window {
#my ($self) = @_;
##$_->destroy for @{ $self->{tabs} };
#1
#}
#This is if you're using the tabbed plugin, of course.
