from .base import SetupPyRecipe


class DateUtilRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(DateUtilRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e27001de32f627c22380a688bcc43ce8' \
                      '3504a7bc5da472209b4c70f02829f0b8'

        self.name = 'dateutil'
        self.pydepends = ['setuptools_scm', 'six']
        self.version = '2.7.3'
        self.pypi_name = 'python-dateutil'
        self.url = 'https://files.pythonhosted.org/packages/a0/b0/' \
                   'a4e3241d2dee665fea11baec21389aec688' \
                   '6655cd4db7647ddf96c3fad15/python-dateutil-$version.tar.gz'
