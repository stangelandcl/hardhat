import os
import shutil
from .base import GnuRecipe


class NginxAuthLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxAuthLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '80d6cce9a9877d51dec2f85a11ce7cd2' \
                      '5edbd2d605c28bc28687ecc5695229ee'
        self.name = 'nginx-auth-ldap'
        self.version = '9f8b59263f6bf36ddfc831554d6b05579794aa9e'
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

