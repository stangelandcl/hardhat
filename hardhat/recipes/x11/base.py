from ..base import GnuRecipe


class X11BaseRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(X11BaseRecipe, self).__init__(*args, **kwargs)
        self.url = 'http://ftp.x.org/archive/individual/lib/' \
                   '$name-$version.tar.bz2'

        self.configure_args += ['--disable-malloc0returnsnull']


class X11AppBaseRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(X11AppBaseRecipe, self).__init__(*args, **kwargs)
        self.url = 'http://ftp.x.org/pub/individual/app/' \
                   '$name-$version.tar.bz2'
        self.depends = ['libpng', 'mesa', 'xbitmaps', 'xcb-util']
        # -P needed so filenames.sed does not result in unterminated strings
        # (from LFS)

    def patch(self):
        if self.name == 'luit' or self.name.startswith('sessreg'):
            self.environment['CPPFLAGS'] += ' -D_XOPEN_SOURCE=600 -P'
            self.environment['CFLAGS'] += ' -D_XOPEN_SOURCE=600'
            self.environment['CXXFLAGS'] += self.environment['CFLAGS']


class X11DataBaseRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(X11DataBaseRecipe, self).__init__(*args, **kwargs)
        self.url = 'http://ftp.x.org/pub/individual/data/' \
                   '$name-$version.tar.bz2'
        self.configure_args += ['--disable-malloc0returnsnull']


class X11DriverBaseRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(X11DriverBaseRecipe, self).__init__(*args, **kwargs)
        self.url = 'http://ftp.x.org/pub/individual/driver/' \
                   '$name-$version.tar.bz2'
        self.configure_args += ['--disable-malloc0returnsnull']
