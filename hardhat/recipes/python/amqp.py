from .base import PipBaseRecipe


class AmqpRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AmqpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2dea4d16d073c902c3b89d9b96620fb6' \
                      '729ac0f7a923bbc777cb4ad827c0c61a'

        self.name = 'amqp'
        self.version = '1.4.9'
