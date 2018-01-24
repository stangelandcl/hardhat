import os
from .base import GnuRecipe
from ..util import patch


class NginxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8410b6c31ff59a763abf7e5a5316e762' \
                      '9f5a5033c95a3a0ebde727f9ec8464c5'

        self.name = 'nginx'
        self.depends = ['nginx-auth-ldap', 'openssl', 'pcre', 'zlib']
        self.version = '1.13.8'
        self.url = 'http://nginx.org/download/nginx-$version.tar.gz'
        self.configure_strip_cross_compile()
        self.configure_args += [
            '--add-module=%s/build/nginx-auth-ldap' % self.prefix_dir,
            '--pid-path=/run/nginx.pid',
            '--error-log-path=/var/log/nginx/error.log',
            '--http-log-path=/var/log/nginx/access.log',
            '--conf-path=%s/etc/nginx/nginx.conf' % self.prefix_dir,
            '--lock-path=/var/log/nginx/nginx.lock',
            '--with-ipv6',
            '--with-pcre',
            '--with-threads',
            '--with-stream',
            '--with-stream_ssl_module',
            '--with-http_ssl_module',
            '--with-http_v2_module',
            '--with-http_gzip_static_module',
            '--with-http_auth_request_module']



    def patch(self):
        self.log_dir('patch', self.directory, 'remove root directory creation')

        filename = os.path.join(self.directory, 'auto', 'install')
        src = r"""	test -d '\$(DESTDIR)`dirname "$NGX_PID_PATH"`' \\
		|| mkdir -p '\$(DESTDIR)`dirname "$NGX_PID_PATH"`'

	test -d '\$(DESTDIR)`dirname "$NGX_HTTP_LOG_PATH"`' \\
		|| mkdir -p '\$(DESTDIR)`dirname "$NGX_HTTP_LOG_PATH"`'"""
        dst = ''
        patch(filename, src, dst)

        src = r"""	test -d '\$(DESTDIR)`dirname "$NGX_ERROR_LOG_PATH"`' \\
		|| mkdir -p '\$(DESTDIR)`dirname "$NGX_ERROR_LOG_PATH"`'"""
        dst = ''
        patch(filename, src, dst)
