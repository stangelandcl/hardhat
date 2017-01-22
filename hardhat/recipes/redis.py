from .base import GnuRecipe


class RedisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RedisRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2e1831c5a315e400d72bda4beaa98c0c' \
                      'fbe3f4eb8b20c269371634390cf729fa'

        self.name = 'redis'
        self.version = '3.2.6'
        self.url = 'http://download.redis.io/releases/redis-$version.tar.gz'
        self.install_args = ['make', 'install', 'PREFIX=%s' % self.prefix_dir]
