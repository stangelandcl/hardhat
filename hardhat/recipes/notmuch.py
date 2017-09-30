from .base import GnuRecipe


class NotMuchRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NotMuchRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b4bf09ec9b7b64180704faa26d66cad5' \
                      'f911a5a00ef812da34cb02c3f8872831'

        self.name = 'notmuch'
        self.version = '0.25.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://notmuchmail.org/releases'
        self.depends = ['autotools', 'gmime', 'python3-sphinx',
                        'talloc', 'xapian']
        self.url = 'https://notmuchmail.org/releases/notmuch-$version.tar.gz'
        self.configure_args += ['--without-ruby']
        # needed to make sphinx test pass to install manpages
        self.environment['PYTHON'] = 'python3'
