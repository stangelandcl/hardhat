from .base import PipBaseRecipe


class WebEncodingsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(WebEncodingsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a5c55ee93b24e740fe951c37b5c228dc' \
                      'cc1f171450e188555a775261cce1b904'

        self.name = 'webencodings'
        self.version = '0.5'
