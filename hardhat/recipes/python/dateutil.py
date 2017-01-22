from .base import PipBaseRecipe


class DateUtilRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DateUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '62a2f8df3d66f878373fd0072eacf4ee' \
                      '52194ba302e00082828e0d263b0418d2'

        self.name = 'dateutil'
        self.pydepends = ['six']
        self.version = '2.6.0'
        self.pypi_name = 'python-dateutil'
