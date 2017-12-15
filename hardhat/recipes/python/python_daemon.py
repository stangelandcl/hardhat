from .base import PipBaseRecipe


class PythonDaemonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonDaemonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '261c859be5c12ae7d4286dc6951e87e9' \
                      'e1a70a882a8b41fd926efc1ec4214f73'
        self.name = 'python-daemon'
        self.version = '2.1.2'  # < 2.2 for apache-airflow
        self.pydepends = ['lockfile']
