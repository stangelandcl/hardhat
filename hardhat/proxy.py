import os
from .util import Object
from hardhat.terminal import Terminal
from threading import Thread


try:
    from urllib.request import ProxyHandler, build_opener, Request
    from urllib.request import install_opener
    from urllib.parse import urlparse
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from urllib2 import ProxyHandler, build_opener, install_opener, Request
    from urlparse import urlparse
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

CACHE_PROXY_PORT = 19992

class Requestor(Object):
    def __init__(self):
        http_proxy = os.environ.get('http_proxy',
                                    os.environ.get('HTTP_PROXY'))
        https_proxy = os.environ.get('https_proxy',
                                     os.environ.get('HTTPS_PROXY'))
        ftp_proxy = os.environ.get('ftp_proxy',
                                   os.environ.get('FTP_PROXY'))

        proxy = dict()
        if http_proxy:
            proxy['http'] = http_proxy
        if https_proxy:
            proxy['https'] = https_proxy
        if ftp_proxy:
            proxy['ftp_proxy'] = ftp_proxy

        self.proxy_handler = ProxyHandler(proxy)
        self.opener = build_opener(self.proxy_handler)

    def request(self, url):
        request = Request(url)
        return self.opener.open(request)


class CacheProxyRequestor(Object):
    def __init__(self, host, port):
        self.url = 'http://%s:%s' % (host, port)
        env = {'http': self.url,
               'https': self.url,
               'ftp': self.url
              }
        self.proxy_handler = ProxyHandler(env)
        self.opener = build_opener(self.proxy_handler)

    def request(self, url):
        request = Request(url)
        return self.opener.open(request)


class CacheProxyHandler(BaseHTTPRequestHandler):

    def _get_filename(self):
        dir = self.server.directory
        path = urlparse(self.path)
        host = path.hostname
        path = path.path

        while len(path) and path[0] == '/':
            path = path[1:]

        host_dir = os.path.join(dir, host)
        return os.path.join(dir, host_dir, path)

    def _check_directory(self, file):
        dirname = os.path.dirname(file)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

    def _download_file(self, file):
        requestor = self.server.requestor
        tmp = file + '.tmp'
        with open(tmp, 'wb') as dst:
            src = requestor.request(self.path)
            while True:
                c = src.read(4096)
                if not c:
                    break
                dst.write(c)
        os.rename(tmp, file)

    def do_GET(self):
        path = Terminal.light_green(self.path)
        print('proxy_path=%s' % (path))

        filename = self._get_filename()
        self._check_directory(filename)
        if not os.path.exists(filename):
            ui_path = Terminal.normal_red(self.path)
            print('cache miss. downloading: %s' % (ui_path))
            self._download_file(filename)

        self.send_response(200)
        self.end_headers()
        with open(filename, 'rb') as f:
            while True:
                c = f.read(4096)
                if not c:
                    break
                self.wfile.write(c)


class CacheProxyServer(HTTPServer):
    def __init__(self, directory, address, handler_class):
        HTTPServer.__init__(self, address, handler_class)
        self.directory = directory
        self.requestor = Requestor()


class Proxy(Object):
    def __init__(self, directory, port=19992):
        self.directory = directory
        self.port = port
        self.host = '127.0.0.1'
        self.requestor = CacheProxyRequestor(self.host, port)

    @property
    def url(self):
        return self.requestor.url

    def __enter__(self):
        address = (self.host, self.port)
        self.proxy = CacheProxyServer(self.directory,
                                      address,
                                      CacheProxyHandler)
        self.thread = Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
        return self

    def _run(self):
        self.proxy.serve_forever(poll_interval=.1)

    def __exit__(self, x, y, z):
        self.proxy.shutdown()
