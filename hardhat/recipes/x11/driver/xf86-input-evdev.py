from ..base import X11DriverBaseRecipe


class Xf86InputEvDevRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86InputEvDevRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9edaa6205baf6d2922cc4db3d8e54a7e' \
                      '7773b5f733b0ae90f6be7725f983b70d'

        self.name = 'xf86-input-evdev'
        self.version = '2.10.5'
        self.depends = ['libevdev', 'mtdev', 'xorg-server']
