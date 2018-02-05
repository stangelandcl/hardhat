from .base import PipBaseRecipe


class ReadmeRendererRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ReadmeRendererRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9deab442963a63a71ab494bf581b1c84' \
                      '4473995a2357f4b3228a1df1c8cba8da'
        self.name = 'readme_renderer'
        self.version = '17.2'
        self.pydepends = ['bleach', 'docutils']
