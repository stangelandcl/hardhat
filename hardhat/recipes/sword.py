import os
from .base import GnuRecipe
from ..util import patch


class Extra:
    def __init__(self, name, sha256=None):
        self.name = 'sword-' + name
        self.sha256 = sha256
        self.version = '1'
        self.url = 'http://www.crosswire.org/ftpmirror/pub/sword/' \
                   'packages/rawzip/%s.zip' % name

class SwordRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwordRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3a573a60339a84ba30daceb415047489' \
                      '2a32c9280660c050123bd16a4251facc'

        self.name = 'sword'
        self.version = 'a9c82c14cb6a49f163ef3042c99bd06321a11d49'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = self.github_commit('greg-hellings')
        self.configure_args = [['./autogen.sh'],
                                ['autoreconf', '-i'],
                                self.configure_args + ['--with-zlib',
                                 '--with-bzip2',
                                 '--with-xz',
                                 '--with-icu',
                                 '--with-conf',
                                 '--with-cxx11regex',
                                 '--with-curl',
                                 '--with-curl_sftp',
                                 '--with-xapian',
                                 '--enable-utilities',
                                 '--disable-tests']]

        self.extra_downloads = [
            Extra('ASV', '9c04c26ca6403212241ba06b227824e6' \
                         'b03a65ef8d08636b7debfc5940f45789'),
            Extra('ESV2001', '29b98d147c9f5ff36e0d78a9a88816d4' \
                             'd8d92f2e65dbd80ab80c0ab97f874009'),
            Extra('ESV2011', 'c3944bb8b2265c44fe58324fee255087' \
                             'fbde42447c3718eea353806c07359f60'),
            Extra('GodsWord', 'b78b3fe857c00d4ccd988b72cd9e9474' \
                             '29e4689b4b9d023a83fc901ebd41b8b8'),
            Extra('KJVA', '5a4773d8512b465e8fd530ff09292ff8' \
                          '364b75b70095184d74260ccbde1b962a'),
            Extra('NETfree', '5f95ee1438835f7a3f1ebc75b0e04d15' \
                             '256f5d5e591586109c07eeff5d1b0b9d'),
            Extra('OEB', 'bb23ead923a400f2f84cb3a9b4c86082' \
                         'c3ff5ef4e3b7098aaa452297d9b7053e'),
            Extra('WEB', '8da1246ec76f2adc62471a91af10062f' \
                         '4265c3fad0bac2a5b21c14e7717fe45a'),
            Extra('YLT', 'd29610d52efb1979e106dfc21337e8f3' \
                         '31e5d421c20836a183ea8656684e0892')
            ]

    def install(self):
        super(SwordRecipe, self).install()

        self.log_dir('install', self.directory, 'installing modules')
        dst = os.path.join(self.prefix_dir, 'share', 'sword')

        for mod in self.extra_downloads:
            args = ['unzip', '-d', dst, mod.filename]
            self.log_dir('install', self.directory,
                         'running %s' % ' '.join(args))
            self.run_exe(args, self.directory, self.environment)
