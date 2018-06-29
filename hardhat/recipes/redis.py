from .base import GnuRecipe


class RedisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RedisRecipe, self).__init__(*args, **kwargs)
        self.name = 'redis'
        self.version = '4.0.10'
        self.url = 'http://download.redis.io/releases/redis-$version.tar.gz'
        self.install_args = ['make', 'install', 'PREFIX=%s' % self.prefix_dir]
