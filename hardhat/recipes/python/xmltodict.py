from .base import PipBaseRecipe


class XmlToDictRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XmlToDictRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fc518ccf9adbbb917a2ddcb386be852a' \
                      'e6dd36935e1e8b9a3e760201abfdbf77'

        self.name = 'xmltodict'
        self.version = '0.10.2'
