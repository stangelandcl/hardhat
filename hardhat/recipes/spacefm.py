from .base import GnuRecipe


class SpaceFMRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SpaceFMRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd3f14fd1b1cfb51df98ebc341ab78ce7' \
                      '41ba443ae2ce9e1662de39d01a95e0f3'

        self.description = 'Fast lightweight file manager'
        self.name = 'spacefm'
        self.version = '1.0.5'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['ffmpegthumbnailer', 'gtk3', 'eudev']
        self.url = self.github_commit('IgnorantGuru', 'spacefm')
