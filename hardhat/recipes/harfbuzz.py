from .base import GnuRecipe


class HarfbuzzRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HarfbuzzRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '21a78b81cd20cbffdb04b59ac7edfb41' \
                      '0e42141869f637ae1d6778e74928d293'

        self.name = 'harfbuzz'
        self.configure_args += ['--with-graphite2=yes']  # required for texlive
        # glib needed for hg-glib.h used by pango
        self.depends = [
                        'freetype',
                        'glib',
                        'graphite2',
                        'icu']
        self.version = '1.4.6'
        self.url = 'http://www.freedesktop.org/software/$name/release/' \
                   '$name-$version.tar.bz2'

    def install(self):
        super(HarfbuzzRecipe, self).install()

        self.log_dir('install', self.prefix_dir, 'reinstalling freetype')
        self.installer.reinstall('freetype')
