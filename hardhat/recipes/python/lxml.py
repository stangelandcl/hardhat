from .base import PipBaseRecipe


class LxmlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LxmlRecipe, self).__init__(*args, **kwargs)

        self.name = 'lxml'
        self.version = '3.5.0'
        self.sha256 = '349f93e3a4b09cc59418854ab8013d02' \
                      '7d246757c51744bf20069bc89016f578'
