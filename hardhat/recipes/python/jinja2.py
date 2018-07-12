from .base import PipBaseRecipe


class Jinja2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Jinja2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f84be1bb0040caca4cea721fcbbbbd61' \
                      'f9be9464ca236387158b0feea01914a4'

        self.name = 'jinja2'
        self.version = '2.10'  # < 2.9 for apache-airflow
        self.pypi_name = 'Jinja2'
        self.depends = ['python-markupsafe']
