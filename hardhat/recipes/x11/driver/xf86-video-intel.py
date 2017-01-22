from ..base import X11DriverBaseRecipe


class Xf86VideoIntelRecipe(X11DriverBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Xf86VideoIntelRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bbec15a9a6d152eb6ac15c1236830fdb' \
                      '081cd3e60fd69be4e066f9e0f924b37d'
        self.name = 'xf86-video-intel'
        self.version = '20160902'
        self.depends = ['xcb-util', 'xorg-server']
        self.configure_args += ['--enable-kms-only',
                                '--enable-uxa']
        self.url = 'http://anduin.linuxfromscratch.org/BLFS/' \
                   'xf86-video-intel/xf86-video-intel-$version.tar.bz2'

        # Optional from BLFS
#cat >> /etc/X11/xorg.conf.d/20-intel.conf << "EOF"
#Section "Device"
#        Identifier "Intel Graphics"
#        Driver "intel"
#        Option "AccelMethod" "uxa"
#EndSection
#EOF
