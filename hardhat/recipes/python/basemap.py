from .base import SetupPyRecipe


class BasemapRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(BasemapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e07ec2e0d63b24c9aed25a09fe8aff25' \
                      '98f82a85da8db74190bac81cbf104531'                

        self.depends = ['geos']
        self.pydepends = ['matplotlib', 'numpy']
        self.name = 'basemap'
        self.version = '1.0.7'
        self.url = 'https://downloads.sourceforge.net/project/matplotlib/' \
                   'matplotlib-toolkits/basemap-$version/basemap-$version.tar.gz'

        self.environment['GEOS_DIR'] = self.prefix_dir
