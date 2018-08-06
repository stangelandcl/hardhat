from .base import GnuRecipe


class AttrRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AttrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5ead72b358ec709ed00bbf7a9eaef165' \
                      '4baad937c001c044fe8b74c57f5324e7'
        self.name = 'attr'
        self.version = '2.4.48'
        self.url = 'http://download.savannah.gnu.org/releases/attr/' \
                   'attr-$version.tar.gz'
        self.configure_strip_cross_compile()
        self.install_args += ['install-dev', 'install-lib']

    def patch(self):
        text = r'''sed -i -e 's|/@pkg_name@|&-@pkg_version@|' include/builddefs.in'''
        self.run_patch_script(text)
