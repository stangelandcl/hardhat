from .base import GnuRecipe


class UsbUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(UsbUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '44741af0bae9d402a0ef160a29b2fa70' \
                      '0bb656ab5e0a4b3343d51249c2a44c8c'
        self.name = 'usbutils'
        self.version = '008'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['libusb', 'python2', 'wget']
        self.url = 'https://www.kernel.org/pub/linux/utils/usb/' \
                   '$name/$name-$version.tar.xz'

        self.configure_args = [
            self.shell_args + [
                'sed', "-i", "/^usbids/ s:usb.ids:hwdata/&:", 'lsusb.py'],
            self.shell_args + ['./configure', '--prefix=%s' % self.prefix_dir,
                               '--datadir=%s/share/hwdata' % self.prefix_dir]]

        self.install_args = [
            ['make', 'install'],
            ['install', '-dm755', '%s/share/hwdata/' % self.prefix_dir],
            ['wget', 'http://www.linux-usb.org/usb.ids', '-O',
             '%s/share/hwdata/usb.ids' % self.prefix_dir]]
