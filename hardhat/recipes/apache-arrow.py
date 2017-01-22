from .base import GnuRecipe
import os


class ApacheArrowRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ApacheArrowRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '13dab5ecd4cb44057a57a47b01cf0f5d' \
                      '07d2e7b373ce652355d578d2fe30fb11'

        self.name = 'apache-arrow'
        self.version = '8960a2ed4c0d400be32003beb183f150e019c4ec'
        self.depends = ['cmake', 'flatbuffers', 'googletest']
        self.url = self.github_commit('apache', 'arrow')

        self.environment['GTEST_HOME'] = self.prefix_dir
        self.environment['FLATBUFFERS_HOME'] = self.prefix_dir

        self.configure_args = ['cmake', '..',
                               '-DCMAKE_BUILD_TYPE=Release',
                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir]

    def patch(self):
        dir = os.path.join(self.directory, 'cpp', 'release')
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.directory = dir
