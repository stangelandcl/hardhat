from .base import GnuRecipe


class Extra:
    pass


class OocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(OocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '138121d34dc0a75773231c9487e5a786' \
                      'd428b4d30e965d77348596d12cde30ce'

        self.name = 'ooc'
        self.version = '079f9b970e2bf33bfa613c670c3d88cea99ac26e'
        self.depends = ['gc']
        self.url = self.github_commit('ooc-lang', 'rock')

        self.bootstrap = Extra()
        self.bootstrap.name = 'rock-bootstrap'
        self.bootstrap.version = '0.9.10'
        self.bootstrap.url = 'https://github.com/ooc-lang/rock/releases/' \
                             'download/v$version/' \
                             'rock-$version-bootstrap-only.tar.bz2'
        self.bootstrap.sha256 = '2ee941ab934b7cd893aa42f0af4dd568' \
                                'ef06a4e77c1b22d83c02e3b9fda06783'
        self.extra_downloads.append(self.bootstrap)

        self.install_args += ['MAN_INSTALL_PATH=%s/man/man1']

    def patch(self):
        self.log_dir('patch', self.directory, 'extract bootstrap')
        self.extract_into(self.bootstrap.filename, self.extract_dir)
