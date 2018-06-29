from .base import PipBaseRecipe


class BeautifulSoupRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BeautifulSoupRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '808b6ac932dccb0a4126558f7dfdcf41' \
                      '710dd44a4ef497a0bb59a77f9f078e89'

        self.name = 'beautifulsoup'
        self.pypi_name = 'beautifulsoup4'
        self.version = '4.6.0'
