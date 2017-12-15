from .base import PipBaseRecipe


class CronIterRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CronIterRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '272c333ab0b354a82173e502d419299e' \
                      '2f3dfdd5dce771ecd8bdf03680495016'

        self.pythons = ['python3']
        self.name = 'croniter'
        self.version = '0.3.20'
