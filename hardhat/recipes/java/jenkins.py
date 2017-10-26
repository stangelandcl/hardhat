import os
from .base import JarBase


class JenkinsRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(JenkinsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f6d1351beef34d980b32f8c463be5054' \
                      '45f637e2fc62156fecd42891c53c97d3'

        self.name = 'jenkins'
        self.version = '2.73.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://mirrors.jenkins.io/war-stable/'
        self.url = 'http://mirrors.jenkins.io/war-stable/$version/jenkins.war'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'jenkins.war')
