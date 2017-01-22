from .base import GnuRecipe
from hardhat.urls import Urls


class GrpcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GrpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd02235dff278869e94cb0dcb31cfea93' \
                      '5693c6f87bd73f43d44147185e6becdd'

        self.name = 'grpc'
        self.version = '0.15.0'
        self.depends = ['cmake']
        version = self.version.replace('.', '_')
        self.url = Urls.github_commit('grpc', self.name,
                                      'release-%s' % version)

        self.environment['AR'] += ' rcs'

    def configure(self):
        pass
