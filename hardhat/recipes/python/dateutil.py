from .base import PipBaseRecipe


class DateUtilRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DateUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e27001de32f627c22380a688bcc43ce8' \
                      '3504a7bc5da472209b4c70f02829f0b8'

        self.name = 'dateutil'
        self.pydepends = ['six']
        self.version = '2.7.3'
        self.pypi_name = 'python-dateutil'
