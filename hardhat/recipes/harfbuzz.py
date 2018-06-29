from .base import GnuRecipe


class HarfbuzzRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HarfbuzzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fbed6392ddb085e45e6090a9f389f729' \
                      '26d0e355f4b0a2ef51d35cf21686df45'

        self.name = 'harfbuzz'
        self.configure_args += ['--with-graphite2=yes']  # required for texlive
        # glib needed for hg-glib.h used by pango
        self.depends = [
                        'freetype',
                        'glib',
                        'graphite2',
                        'icu']
        self.version = '1.8.1'
        self.url = 'http://www.freedesktop.org/software/$name/release/' \
                   '$name-$version.tar.bz2'

    def install(self):
        super(HarfbuzzRecipe, self).install()

        self.log_dir('install', self.prefix_dir, 'reinstalling freetype')
        self.installer.reinstall('freetype')
