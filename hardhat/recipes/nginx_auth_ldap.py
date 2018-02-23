import os
import shutil
from .base import GnuRecipe


class NginxAuthLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxAuthLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e3cfe3a05c6d0bf34df3f64dcf72a4d2' \
                      '2e4c408817da7ab2f13989d73a4160f3'
                
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

