from ..base import X11DriverBaseRecipe


class Xf86VideoAtiRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86VideoAtiRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '401f5de772928f3dc4ce43a885adb0a4' \
                      '7a2f61aa4a9e45d2ab3d184136a9d6fa'

        self.name = 'xf86-video-ati'
        self.version = '7.8.0'
        self.depends = ['xorg-server']
