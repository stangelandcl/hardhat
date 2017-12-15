from .base import PipBaseRecipe


class ApacheAirflowRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ApacheAirflowRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e18e00d07c6c23c16c53bbfac87fc520' \
                      'e626119bb0123dca84076e83129ad4a3'

        self.pythons = ['python3']
        self.pydepends = [
            'alembic',
            'bleach',
            'configparser',  # [3.5.0, 3.6.0)
            'croniter',
            'docutils',
            'dill',
            'flask',
            'flask-admin',
            'flask-cache',
            'flask-login',
            'flask-swagger',
            'flask-wtf',
            'funcsigs',
            'future',
            'gitpython',
            'gunicorn',  # < 20.0
            'iso8601',
            'jinja2',
            'lxml',
            'markdown',
            'pandas',
            'pendulum',
            'psutil',
            'pygments',
            'python-daemon',
            'python-dateutil',
            'python-nvd3',
            'requests',
            'setproctitle',
            'sqlalchemy',
            'sqlalchemy-utc',
            'tabulate',
            'thrift',
            'tzlocal',
            'zope.deprecation',  # < 5.0
            ]
        self.name = 'apache-airflow'
        self.version = '1.8.2'
