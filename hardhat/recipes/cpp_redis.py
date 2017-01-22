from .base import GnuRecipe


class CppRedisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CppRedisRecipe, self).__init__(*args, **kwargs)
        self.name = 'cpp_redis'
        self.version = '2.2'
        self.url = 'https://github.com/Cylix/cpp_redis/archive/2.2.tar.gz'
