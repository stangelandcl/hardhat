from hardhat.recipes.base import GnuRecipe


class XInitRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XInitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '75d88d7397a07e01db253163b7c7a00b' \
                      '249b3d30e99489f2734cac9a0c7902b3'

        self.name = 'xinit'
        self.version = '1.3.4'
        self.depends = ['xorg-server']
        self.url = 'http://ftp.x.org/pub/individual/app/xinit-$version.tar.bz2'

        self.configure_args += [
            '--with-xinitdir=%s/etc/X11/app-defaults' % self.prefix_dir]

