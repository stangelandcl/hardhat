from ..base import X11DriverBaseRecipe


class Xf86VideoNouveauRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86VideoNouveauRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6d9242ba139c3df7afefffb455573b52' \
                      'f4427920b978161c00483c64a6da47cb'

        self.name = 'xf86-video-nouveau'
        self.version = '1.0.13'
        self.depends = ['xorg-server']
