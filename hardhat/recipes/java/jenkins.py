import os
from .base import JarBase


class JenkinsRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(JenkinsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'aa7f243a4c84d3d6cfb99a218950b8f7' \
                      'b926af7aa2570b0e1707279d464472c7'
                
        self.name = 'jenkins'
        self.version = '2.46.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://mirrors.jenkins.io/war-stable/'
        self.url = 'http://mirrors.jenkins.io/war-stable/$version/jenkins.war'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'jenkins.war')
