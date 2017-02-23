from .base import GnuRecipe


class TinyProxyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TinyProxyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a41f4ddf0243fc517469cf444c8400e1' \
                      'd2edc909794acda7839f1d644e8a5000'
                
        self.name = 'tinyproxy'
        self.version = '1.8.4'
        self.url = 'https://github.com/tinyproxy/tinyproxy/releases/' \
                   'download/$version/tinyproxy-$version.tar.xz'
        self.configure_strip_cross_compile()

    def install(self):
        super(TinyProxyRecipe, self).install()
        self.log_dir('install', self.directory, 'install config file')

        config = r'''
port=47010
listen=127.0.0.1
'''
        filename = os.path.join(self.prefix_dir, 'etc', 'tinyproxy', 'tinyproxy.conf')
        dir = os.path.dirname(filename)
        if not os.path.exists(dir):
            os.makedirs(dir)

        with open(filename, 'wt') as f:
            f.write(config)
        
