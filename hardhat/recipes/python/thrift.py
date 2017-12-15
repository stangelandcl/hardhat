from .base import PipBaseRecipe


class ThriftRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ThriftRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dfbc3d3bd19d396718dab05abaf46d93' \
                      'ae8005e2df798ef02e32793cd963877e'
        self.name = 'thrift'
        self.version = '0.9.3'  # < 0.10 for apache-airflow
