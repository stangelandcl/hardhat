from .base import GnuRecipe


class AttrRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AttrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '25772f653ac5b2e3ceeb89df50e46888' \
                      '91e21f723c460636548971652af0a859'

        self.name = 'attr'
        self.version = '2.4.47'
        self.url = 'http://download.savannah.gnu.org/releases/attr/' \
                   'attr-$version.src.tar.gz'
        self.configure_strip_cross_compile()
        self.install_args += ['install-dev', 'install-lib']

    def patch(self):
        text = r'''sed -i -e 's|/@pkg_name@|&-@pkg_version@|' include/builddefs.in'''
        self.run_patch_script(text)
