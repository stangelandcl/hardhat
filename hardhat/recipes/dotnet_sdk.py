import os
import shutil
from .base import GnuRecipe
from ..util import write_script


class DotnetSdkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DotnetSdkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2a9e0ed251a7f98a46473f694532acdc' \
                      '5a0960d32204e82315c38c1b29fdd317'
        self.name = 'dotnet-sdk'
        self.version = '2.0.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://download.microsoft.com/download/7/3/A/' \
                   '73A3E4DC-F019-47D1-9951-0453676E059B/' \
                   'dotnet-sdk-$version-linux-x64.tar.gz'

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy tree and create script')
        dst = os.path.join(self.prefix_dir, 'dotnet')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        os.rename(self.directory, dst)

        script = r'''#!/bin/sh
# MSBuildEmitSolution is required for project ordering dependencies
# in a solution to work. It causes a *.sln.metaproj to be created
# in one step which is used in another step
export MSBuildEmitSolution=true
%s/dotnet "$@"
''' % dst
        filename = os.path.join(self.prefix_dir, 'bin', 'dotnet')
        write_script(filename, script)
