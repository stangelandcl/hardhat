from .base import GnuRecipe


class LibmtpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibmtpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '494ee02fbfbc316aad75b93263dac00f' \
                      '02a4899f28cfda1decbbd6e26fda6d40'
        self.name = 'libmtp'
        self.version = '1.1.13'
        self.depends = ['autotools']
        self.url = 'https://downloads.sourceforge.net/project/$name/' \
                   '$name/$version/$name-$version.tar.gz'

        # TODO: requires sudo to install mtp-probe in udev
