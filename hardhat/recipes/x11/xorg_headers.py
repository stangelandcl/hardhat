from ..base import LogConfigure, LogDownloader, LogExtractor, Logger
from ..base import Recipe, LogMakeInstall


class XOrgHeadersRecipe(Recipe):
    def __init__(self, *args, **kwargs):
        super(XOrgHeadersRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2835b11829ee634e19fa56517b4cfc52' \
                      'ef39acea0cd82e15f68096e27cbed0ba'

        self.name = 'xorg-headers'
        self.version = '0.1'
        self.url = 'http://ftp.x.org/pub/individual/proto/'

        self.files = [
            ('bigreqsproto', '1.1.2', '462116ab44e41d8121bfde9473219503'
                                      '70b285a5316612b8fce8334d50751b1e'),
            ('compositeproto', '0.4.2', '049359f0be0b2b984a8149c966dd04e8'
                                        'c58e6eade2a4a309cf1126635ccd0cfc'),
            ('damageproto', '1.2.1', '5c7c112e9b9ea8a9d5b019e5f17d481a'
                                     'e20f766cb7a4648360e7c1b46fc9fc5b'),
            ('dmxproto', '2.3.1', 'e72051e6a3e06b236d19eed56368117b'
                                  '745ca1e1a27bdc50fd51aa375bea6509'),
            ('dri2proto', '2.8', 'f9b55476def44fc7c459b2537d17dbc7'
                                 '31e36ed5d416af7ca0b1e2e676f8aa04'),
            ('dri3proto', '1.0', '01be49d70200518b9a6b297131f6cc71'
                                 'f4ea2de17436896af153226a774fc074'),
            ('fixesproto', '5.0', 'ba2f3f31246bdd3f2a0acf8bd3b09ba9'
                                  '9cab965c7fb2c2c92b7dc72870e424ce'),
            ('fontsproto', '2.1.3', '259046b0dd9130825c4a4c479ba3591d'
                                    '6d0f17a33f54e294b56478729a6e5ab8'),
            ('glproto', '1.4.17', 'adaa94bded310a2bfcbb9deb4d751d96'
                                  '5fcfe6fb3a2f6d242e2df2d6589dbe40'),
            ('inputproto', '2.3.1', '5a47ee62053a6acef3a83f506312494b'
                                    'e1461068d0b9269d818839703b95c1d1'),
            ('kbproto', '1.0.6', '037cac0aeb80c4fccf44bf736d791fcc'
                                 'b2ff7fd34c558ef8f03ac60b61085479'),
            ('presentproto', '1.0', '812c7d48721f909a0f7a2cb1e91f6eea'
                                    'd76159a36c4712f4579ca587552839ce'),
            ('randrproto', '1.5.0', '4c675533e79cd730997d232c8894b669'
                                    '2174dce58d3e207021b8f860be498468'),
            ('recordproto', '1.14.2', 'a777548d2e92aa259f1528de3c4a36d1'
                                      '5e07a4650d0976573a8e2ff5437e7370'),
            ('renderproto', '0.11.1', '06735a5b92b20759204e4751ecd6064a'
                                      '2ad8a6246bb65b3078b862a00def2537'),
            ('resourceproto', '1.2.0', '3c66003a6bdeb0f70932a9ed3cf57cc5'
                                       '54234154378d301e0c5cfa189d8f6818'),
            ('scrnsaverproto', '1.2.2', '8bb70a8da164930cceaeb4c741802916'
                                        '60533ad3cc45377b30a795d1b85bcd65'),
            ('videoproto', '2.3.3', 'c7803889fd08e6fcaf7b68cc394fb038'
                                    'b2325d1f315e571a6954577e07cca702'),
            ('xcmiscproto', '1.2.2', 'b13236869372256c36db79ae39d54214'
                                     '172677fb79e9cdc555dceec80bd9d2df'),
            ('xextproto', '7.3.0', 'f3f4b23ac8db9c3a9e0d8edb591713f3'
                                   'd70ef9c3b175970dd8823dfc92aa5bb0'),
            ('xf86bigfontproto', '1.2.0', 'ba9220e2c4475f5ed2ddaa7287426b30'
                                          '089e4d29bd58d35fad57ba5ea43e1648'),
            ('xf86dgaproto', '2.1', 'ac5ef65108e1f2146286e53080975683'
                                    'dae49fc94680042e04bd1e2010e99050'),
            ('xf86driproto', '2.1.1', '9c4b8d7221cb6dc4309269ccc008a227'
                                      '53698ae9245a398a59df35f1404d661f'),
            ('xf86vidmodeproto', '2.3.1', '45d9499aa7b73203fd6b3505b0259624'
                                          'afed5c16b941bd04fcf123e5de698770'),
            ('xineramaproto', '1.2.1', '977574bb3dc192ecd9c55f59f991ec1d'
                                       'ff340be3e31392c95deff423da52485b'),
            ('xproto', '7.0.31', 'c6f9747da0bd3a95f86b17fb8dd5e717'
                                 'c8f3ab7f0ece3ba1b247899ec1ef7747'),
            ]

    def _create_downloaders(self):
        downloaders = []
        for name, version, sha256 in self.files:
            downloader = LogDownloader(settings=self)
            downloader.name = name
            downloader.version = version
            downloader.environment = self.environment
            downloader.url = self.url + name + '-' + version + '.tar.bz2'
            downloader.sha256 = sha256
            downloaders.append(downloader)
        return downloaders

    def download(self):
        for downloader in self._create_downloaders():
            downloader.download()

    def _create_extractors(self):
        self.filenames = list(map(lambda x: x.filename,
                                  self._create_downloaders()))

        extractors = []
        for i in range(len(self.files)):
            name, version, sha256 = self.files[i]
            tarball = self.filenames[i]

            extractor = LogExtractor()
            extractor.prefix_dir = self.prefix_dir
            extractor.name = name
            extractor.version = version
            extractor.filename = tarball
            extractors.append(extractor)
        return extractors

    def clean(self):
        e = self._create_extractors()
        for extractor in e:
            extractor.clean()

    def extract(self):
        self.extracted = []
        for extractor in self._create_extractors():
            extractor.extract()
            self.extracted.append(extractor.extract_dir)

    def configure(self):
        for i in range(len(self.extracted)):
            configure = LogConfigure()
            name, version, sha256 = self.files[i]
            configure.quiet = self.quiet
            configure.name = name
            configure.version = version
            configure.shell_args = self.shell_args
            configure.environment = self.environment
            configure.prefix_dir = self.prefix_dir
            configure.build_triplet = self.build_triplet
            configure.host_triplet = self.host_triplet
            configure.directory = self.extracted[i]
            configure.configure()

    def compile(self):
        pass

    def install(self):
        for i in range(len(self.extracted)):
            extracted = self.extracted[i]
            install = LogMakeInstall()
            name, version, sha256 = self.files[i]
            install.prefix_dir = self.prefix_dir
            install.quiet = self.quiet
            install.name = name
            install.version = version
            install.environment = self.environment
            install.directory = extracted
            install.install()
