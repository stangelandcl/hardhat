from .base import PipBaseRecipe


class SetProcTitleRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SetProcTitleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6283b7a58477dd8478fbb9e76defb379' \
                      '68ee4ba47b05ec1c053cb39638bd7398'
        self.name = 'setproctitle'
        self.version = '1.1.10'  # < 2 for apache-airflow
