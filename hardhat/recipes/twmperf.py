from .base import GnuRecipe


class TwemPerfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TwemPerfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3662daef512b6f3709fc211de40471a7' \
                      '38940352f5a787bfc21e9eecbb55b387'

        self.name = 'twemperf'
        self.description = 'memcached performance tester in C'
        self.version = '0.1.1'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/twitter/twemperf/' \
                           'releases'
        self.url = 'https://github.com/twitter/twemperf/archive/' \
                   'v$version.tar.gz'
        self.doc = r'''
    The following example creates 1000 connections to a memcached server running on localhost:11211. The connections are created at the rate of 1000 conns/sec and on every connection it sends 10 'set' requests at the rate of 1000 reqs/sec with the item sizes derived from a uniform distribution in the interval of [1,16) bytes.

$ mcperf --linger=0 --timeout=5 --conn-rate=1000 --call-rate=1000 --num-calls=10 --num-conns=1000 --sizes=u1,16
'''

    def configure(self):
        self.configure_args = ['autoreconf', '-i']
        super(TwemPerfRecipe, self).configure()

        self.configure_args = self.shell_args + [
            'configure',
            '--prefix=%s' % self.prefix_dir]
        super(TwemPerfRecipe, self).configure()
