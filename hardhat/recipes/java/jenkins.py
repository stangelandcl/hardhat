import os
from .base import JarBase


class JenkinsRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(JenkinsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'efbb4360de55947189f67895be0960dd' \
                      'fd75104732802948f082f8a5e93228ca'

        self.name = 'jenkins'
        self.version = '2.32.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://mirrors.jenkins.io/war-stable/'
        self.url = 'http://mirrors.jenkins.io/war-stable/$version/jenkins.war'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'jenkins.war')
