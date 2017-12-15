from .base import PipBaseRecipe


class Jinja2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Jinja2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '35341f3a97b46327b3ef1eb624aadea8' \
                      '7a535b8f50863036e085e7c426ac5891'
        self.name = 'jinja2'
        self.version = '2.8.1'  # < 2.9 for apache-airflow
        self.pypi_name = 'Jinja2'
        self.depends = ['python-markupsafe']
