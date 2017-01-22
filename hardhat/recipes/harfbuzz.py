from .base import GnuRecipe


class HarfbuzzRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HarfbuzzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '718aa6fcadef1a6548315b8cfe42cc27' \
                      'e926256302c337f42df3a443843f6a2b'

        self.name = 'harfbuzz'
        self.configure_args += ['--with-graphite2=yes']  # required for texlive
        # glib needed for hg-glib.h used by pango
        self.depends = [
                        'freetype',
                        'glib',
                        'graphite2',
                        'icu']
        self.version = '1.3.4'
        self.url = 'http://www.freedesktop.org/software/$name/release/' \
                   '$name-$version.tar.bz2'

    def install(self):
        super(HarfbuzzRecipe, self).install()

        self.log_dir('install', self.prefix_dir, 'reinstalling freetype')
        self.installer.reinstall('freetype')
