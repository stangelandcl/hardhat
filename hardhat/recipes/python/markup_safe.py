from .base import PipBaseRecipe


class MarkupSafeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MarkupSafeRecipe, self).__init__(*args, **kwargs)

        self.name = 'markupsafe'
        self.version = '0.23'
        self.pypi_name = 'MarkupSafe'
        self.sha256 = 'a4ec1aff59b95a14b45eb2e23761a017' \
                      '9e98319da5a7eb76b56ea8cdc7b871c3'
