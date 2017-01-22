from .base import PipBaseRecipe


class SqlAlchemyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SqlAlchemyRecipe, self).__init__(*args, **kwargs)

        self.name = 'sqlalchemy'
        self.version = '1.0.13'
        self.sha256 = 'e755fd23b8bd574163d392ae85f41f6c' \
                      'd32eca8fe5bd7b5692de77265bb220cf'
