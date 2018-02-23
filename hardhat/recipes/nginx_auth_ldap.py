import os
import shutil
from .base import GnuRecipe


class NginxAuthLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxAuthLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '83938e4ae7bac87440b8ea920987ca2f' \
                      '5407ea86c37b439b61ddfc3ad1347891'        
        self.name = 'nginx-auth-ldap'
        self.version = '12fed6b82954d8b85d17c7e360d35c2d1eb3d3f9'
        self.url = self.github_commit('stangelandcl')

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy')

        dir = os.path.dirname(self.directory)
        dir = os.path.join(dir, 'nginx-auth-ldap')
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)

