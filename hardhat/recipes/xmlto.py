from .base import GnuRecipe


class XmltoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XmltoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1130df3a7957eb9f6f0d29e4aa1c7573' \
                      '2a7dfb6d639be013859b5c7ec5421276'
        
        self.name = 'xmlto'
        self.version = '0.0.28'
        self.url = 'https://launchpad.net/ubuntu/+archive/primary/' \
                   '+files/xmlto_$version.orig.tar.bz2'
