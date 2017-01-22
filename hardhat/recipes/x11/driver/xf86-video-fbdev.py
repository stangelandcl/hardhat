from ..base import X11DriverBaseRecipe


class Xf86VideoFbDevRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86VideoFbDevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9dd4b326498223abbfdf786089a46ea3' \
                      'db4fa6bbd341308eb48a9e00bc3fd51b'

        self.name = 'xf86-video-fbdev'
        self.version = '0.4.4'
        self.depends = ['xorg-server']
