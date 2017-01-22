from .base import PipBaseRecipe


class BilliardRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BilliardRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '692a2a5a55ee39a42bcb7557930e2541' \
                      'da85df9ea81c6e24827f63b80cd39d0b'

        self.name = 'billiard'
        self.version = '3.3.0.23'
