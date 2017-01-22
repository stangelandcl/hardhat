from .gcc_prereq import GccPrereqRecipe


class CrossGccMpfrRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccMpfrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c7e75a08a8d49d2082e4caee1591a05d' \
                      '11b9d5627514e678f02d66a124bcf2ba'
        self.gcc_directory = None
        self.name = 'cross-mpfr'
        self.version = '2.4.2'
