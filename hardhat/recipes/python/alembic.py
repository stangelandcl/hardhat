from .base import PipBaseRecipe


class AlembicRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AlembicRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'de8ca3b1d806cd39bf8a21d90f5c5822' \
                      'a2173b721ec20f868da38edd45b58cb2'
        self.pythons = ['python3']
        self.pydepends = ['mako',
                          'python-dateutil',
                          'python-editor',
                          'sqlalchemy',
                          ]
        self.name = 'alembic'
        self.version = '0.8.5'  # apache-airflow requires < 0.9
