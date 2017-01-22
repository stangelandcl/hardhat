from .base import GnuRecipe


class RabbitMqRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RabbitMqRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b09eadd91244115e50856d1423e4659e' \
                      '46313f1545c69b434021e1afa1b60216'

        self.name = 'rabbitmq'
        self.depends = ['erlang']
        self.version = '3.6.2'
        self.url = 'https://www.rabbitmq.com/releases/rabbitmq-server/' \
                   'v$version/rabbitmq-server-$version.tar.xz'
