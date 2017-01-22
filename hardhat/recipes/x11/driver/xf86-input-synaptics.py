from ..base import X11DriverBaseRecipe


class Xf86InputSynapticsRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86InputSynapticsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'afba3289d7a40217a19d90db98ce1817' \
                      '72f9ca6d77e1898727b0afcf02073b5a'

        self.name = 'xf86-input-synaptics'
        self.version = '1.9.0'
        self.depends = ['libevdev', 'xorg-server']
