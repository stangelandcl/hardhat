from .base import GnuRecipe


class RustRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RustRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f966b31eb1cd9bd2df817c391a338eeb' \
                      '5b9253ae0a19bf8a11960c560f96e8b4'
        self.name = 'rust'
        self.version = '1.16.0'
        self.depends = ['autotools', 'curl', 'cmake', 'python2']
        self.url = 'https://static.rust-lang.org/dist/' \
                   'rustc-$version-src.tar.gz'

        self.configure_args = self.shell_args + [
            './configure',
            '--libdir=%s/lib' % self.prefix_dir,
            '--mandir=%s/share/man' % self.prefix_dir,
            '--docdir=%s/share/doc/rust' % self.prefix_dir,
            '--local-rust-root=%s' % self.prefix_dir,
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--datadir=%s/share' % self.prefix_dir,
            '--infodir=%s/share/info' % self.prefix_dir,
            '--localstatedir=%s/var/lib' % self.prefix_dir,
            '--musl-root=%s' % self.prefix_dir,
            '--prefix=%s' % self.prefix_dir,
            '--target=x86_64-unknown-linux-gnu',
            '--host=x86_64-unknown-linux-gnu']
        self.compile_args = ['python2', './x.py', 'build']
        self.install_args = ['python2', './x.py', 'dist', '--install']
