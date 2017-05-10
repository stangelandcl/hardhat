from .base import PipBaseRecipe


class MarkupSafeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MarkupSafeRecipe, self).__init__(*args, **kwargs)

        self.name = 'markupsafe'
        self.version = '1.0'  # was 0.23
        self.pypi_name = 'MarkupSafe'
