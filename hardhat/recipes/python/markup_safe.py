from .base import PipBaseRecipe


class MarkupSafeRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MarkupSafeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a6be69091dac236ea9c6bc7d012beab4' \
                      '2010fa914c459791d627dad4910eb665'

        self.name = 'markupsafe'
        self.version = '1.0'  # was 0.23
        self.pypi_name = 'MarkupSafe'
