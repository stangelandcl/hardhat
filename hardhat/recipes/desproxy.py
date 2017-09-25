from .base import GnuRecipe


class DesproxyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DesproxyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd0c8a299fc3eacd12aef79c422a09f0e' \
                      '15e48ac69163ff8eef0b62b20d162ffd'

        self.name = 'desproxy'
        self.version = '0.1.0-pre3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://downloads.sourceforge.net/desproxy/files/' \
                   '$name-$version.tar.gz'

r'''
Imagine you're inside a corporation, with a HTTP/1.1 compliant proxy (proxy.corporation.com:8080) that is the only way to get out there... But, hey! you want to chat using your favourite irc server (irc.foo.bar:6667 isn't that?) so you launch "desproxy" this way:

desproxy irc.foo.bar 6667 proxy.corporation.com 8080 6667

Now, desproxy is listening on your local port 6667, waiting for a connection (from your irc client). So you launch xchat, zircon... and type

/server 127.0.0.1 6667

xchat now tries to connect with your local port 6667, desproxy "hears the bell" and after accepting the incoming connection, makes a connection to the irc server (irc.foo.bar 6667) trough the HTTP proxy (proxy.corporation.com 8080). When it gets the connection with the irc server, desproxy hooks the two sockets together, so xchat gets the wellcome message from the irc server as if it were connected to /server irc.foo.bar 6667 .

Usage

Usage: desproxy remote_host remote_port proxy_host proxy_port local_port
'''
