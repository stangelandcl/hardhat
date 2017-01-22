from .base import PipBaseRecipe


class DjangoRestFrameworkFiltersRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DjangoRestFrameworkFiltersRecipe, self).__init__(*args, **kwargs)

        self.name = 'djangorestframework-filters'
        self.version = '0.8.0'
        self.pydepends = ['django', 'djangorestframework']
        self.sha256 = 'c4d77bc01af20cc7551f704f35db5aa8' \
                      '72f6ba717e43ddd21a1de5f448838244'
