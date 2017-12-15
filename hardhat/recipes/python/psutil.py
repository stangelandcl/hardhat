from .base import PipBaseRecipe


class PSUtilRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PSUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1c37e6428f7fe3aeea607f9249986d9b' \
                      'b933bb98133c7919837fd9aac4996b07'
        self.name = 'psutil'
        self.version = '4.4.2'  # < 5 for apache-airflow
