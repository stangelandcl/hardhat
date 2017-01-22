import os
import stat
from .base import GnuRecipe
from ..urls import Urls


class FioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '92520bff7e45750f697366823b81a989' \
                      '9c5150f34fef0414919e9e1110627bd4'

        self.description = 'disk benchmark'
        self.name = 'fio'
        self.version = '2.16'
        self.depends = ['libaio']
        self.url = Urls.github_commit('axboe',
                                      self.name,
                                      self.name + '-' + self.version)
        self.configure_strip_cross_compile()
        self.configure_strip_sysroot()

    def post_install(self):
        test = r'''
[global]
bs=4k
#ioengine=libaio
iodepth=4
size=1g
#direct=1
runtime=60
directory=%s
filename=ssd.test.file

[seq-read]
rw=read
stonewall

[rand-read]
rw=randread
stonewall

[seq-write]
rw=write
stonewall

[rand-write]
rw=randwrite
stonewall

''' % self.tarball_dir

        filename = os.path.join(self.prefix_dir, 'etc', 'fio.job')
        with open(filename, 'wt') as f:
            f.write(test)

        script = r'''#!/bin/bash
        fio ${HARDHAT_PREFIX}/etc/fio.job
'''

        filename = os.path.join(self.prefix_dir, 'bin', 'fio-test')
        with open(filename, 'wt') as f:
            f.write(script)
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
