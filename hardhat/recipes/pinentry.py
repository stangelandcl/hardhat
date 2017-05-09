import os
from .base import GnuRecipe


class PinentryRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PinentryRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1672c2edc1feb036075b187c0773787b' \
                      '2afd0544f55025c645a71b4c2f79275a'

        self.name = 'pinentry'
        self.version = '1.0.0'
        self.url = 'https://www.gnupg.org/ftp/gcrypt/$name/' \
                   '$name-$version.tar.bz2'
        self.environment['LIBS'] += ' -ltinfow'
        self.depends = ['qt5']
