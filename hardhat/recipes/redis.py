from .base import GnuRecipe


class RedisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RedisRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fc53e73ae7586bcdacb4b63875d1ff04' \
                      'f68c5474c1ddeda78f00e5ae2eed1bbb'

        self.name = 'redis'
        self.version = '4.0.11'
        self.url = 'http://download.redis.io/releases/redis-$version.tar.gz'
        self.install_args = ['make', 'install', 'PREFIX=%s' % self.prefix_dir]
