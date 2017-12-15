from .base import PipBaseRecipe


class LockFileRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LockFileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6aed02de03cba24efabcd600b3054014' \
                      '0634fc06cfa603822d508d5361e9f799'
        self.name = 'lockfile'
        self.version = '0.12.2'
