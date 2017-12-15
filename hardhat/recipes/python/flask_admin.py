from .base import PipBaseRecipe


class FlaskAdminRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskAdminRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '88618750e08ceee1ab232a5a9ebcef31' \
                      '275db5db1c0b56db29e014c24c7067a4'
        self.name = 'flask-admin'
        self.version = '1.4.1'  # apache-airflow requirement
        self.pydepends = ['flask', 'wtforms']
