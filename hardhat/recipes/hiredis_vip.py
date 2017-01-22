from .base import GnuRecipe


class HiRedisVipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HiRedisVipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '84e0f9367fa25089fc073b7a8a072504' \
                      '3c48cccec827acf4555a63da68f36be5'

        self.name = 'hiredis-vip'
        self.description = 'redis client'
        self.version = '0.3.0'
        self.url = 'https://github.com/vipshop/hiredis-vip/archive/' \
                   '$version.tar.gz'
