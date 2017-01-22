from .gcc_prereq import GccPrereqRecipe


class GccMpfrRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccMpfrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c7e75a08a8d49d2082e4caee1591a05d' \
                      '11b9d5627514e678f02d66a124bcf2ba'
        self.gcc_directory = None
        self.name = 'mpfr'
        self.version = '2.4.2'
