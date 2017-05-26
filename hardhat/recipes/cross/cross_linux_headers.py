import os
import platform
from hardhat.environment import toolchain_env
from .base import make_cross_prefix_dir, CrossGnuRecipe


def linux_version():
    v = platform.release()
    dots = v.split('.')
    for i in range(len(dots)):
        dots[i] = dots[i].split('-')[0]
    return '.'.join(dots[:3])


def version_compare(x, y):
    x = x.split('.')
    y = y.split('.')

    size = min(len(x), len(y))
    for i in range(size):
        xi = int(x[i])
        yi = int(y[i])
        if xi < yi:
            return -1
        if xi > yi:
            return 1

    if len(x) < len(y):
        return -1

    if len(x) > len(y):
        return 1

    return 0


# (version, sha256, url) in order
VERSIONS = [
# glibc 2.24 requires linux kernel headers 3.2 or better but will still
# work on x64 when the actual kernel is 2.6.32 or better, except on Intel
    ('2.6.32.71',
     '640af1c1a9aad730b1e733f3be3671d503842be42d40adffd2af72dd21ca41be',
     'http://cdn.kernel.org/pub/linux/kernel/v2.6/longterm/v2.6.32/'
     'linux-2.6.32.71.tar.gz'),
    ('3.2.83',
     '999423977616ca6ba2463229f00aee2334ef778f059fdaa84499eeddbcecad01',
     'https://cdn.kernel.org/pub/linux/kernel/v3.x/linux-3.2.83.tar.gz'),
    ('4.1.24',
     '012b86fdf19db3018b6dce50a8f1879b151304b42c6e1b530780d12133d43608',
     'http://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.1.24.tar.gz'),
    ('4.4.6',
     '2999bb9b7728ec62097efaadab60735e52ac5fab9dec006239cd903707960f53',
     'http://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.4.6.tar.gz'),
    ('4.7.10',
     'c314cdfac8e3526201b2911a36fd18bd80f15aead5ca4dcce08d07eb463b04d3',
     'http://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.7.10.tar.gz'),
    ('4.10.14',
     '86b597801ab62c57a8af818cb555009e54b87a16ecb61e665abb974a44e821b6',
     'http://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.10.14.tar.gz')
]


def linux_headers_version():
    v = linux_version()
    i = 0
    for version in VERSIONS:
        c = version_compare(v, version[0])
        if c == 0:
            return version
        if c < 0:
            left = v.split('.')[:2]
            right = v.split('.')[:2]
            if i == 0 or left == right:
                return version
            return VERSIONS[i-1]
        i += 1
    return VERSIONS[-1]


class LinuxHeadersBase(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinuxHeadersBase, self).__init__(*args, **kwargs)
        version, sha256, url = linux_headers_version()
        self.version = version
        self.sha256 = sha256
        self.url = url
        self.configure_args = ['make', 'mrproper']
        self.compile_args = ['make',
                             'INSTALL_HDR_PATH=dest',
                             'headers_install']

    def install(self):
        self.install_args = [
            'cp', '-rv', 'dest/include/*', self.include_dir]
        if not os.path.exists(self.include_dir):
            os.makedirs(self.include_dir)
        super(LinuxHeadersBase, self).install()

    def post_install(self):
        pass


class CrossLinuxHeadersRecipe(LinuxHeadersBase):
    def __init__(self, *args, **kwargs):
        super(CrossLinuxHeadersRecipe, self).__init__(*args, **kwargs)
        self.name = 'cross-linux-headers'
        self.include_dir = '%s/%s/include' % (
            self.cross_prefix_dir,
            self.target_triplet)

    def version_check(self):
        pass
