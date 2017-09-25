from .base import GnuRecipe


class NotMuchRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NotMuchRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '65d28d1f783d02629039f7d15d9a2bad' \
                      'a147a7d3809f86fe8d13861b0f6ae60b'

        self.name = 'notmuch'
        self.version = '0.25'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://notmuchmail.org/releases'
        self.depends = ['autotools', 'gmime', 'talloc', 'xapian']
        self.url = 'https://notmuchmail.org/releases/notmuch-$version.tar.gz'
        self.configure_args += ['--without-ruby']
