from .base import GnuRecipe


class StartupNotificationRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(StartupNotificationRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c391f7e930c583095045cd2d10eb73a' \
                      '64f085c7fde9d260f2652c7cb3cfbe4a'
        self.name = 'startup-notification'
        self.version = '0.12'
        self.depends = ['xcb-util', 'xorg-libs']
        self.url = 'http://www.freedesktop.org/software/' \
                   'startup-notification/releases/' \
                   'startup-notification-$version.tar.gz'
        self.environment['CFLAGS'] += ' -Wno-unused-but-set-variable'
        self.configure_strip_cross_compile()
