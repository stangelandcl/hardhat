from .base import GnuRecipe


class AclRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AclRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '179074bb0580c06c4b4137be4c5a92a7' \
                      '01583277967acdb5546043c7874e0d23'

        self.name = 'acl'
        self.version = '2.2.52'
        self.depends = ['attr']
        self.url = 'http://download.savannah.gnu.org/releases/acl/' \
                   'acl-$version.src.tar.gz'

        self.configure_args += [
            '--libexecdir=%s/lib' % self.prefix_dir]
        self.configure_strip_cross_compile()
        self.install_args += ['install-dev', 'install-lib']

    def patch(self):
        text = r'''sed -i -e 's|/@pkg_name@|&-@pkg_version@|' include/builddefs.in'''
        self.run_patch_script(text)

    def post_install(self):
        super(AclRecipe, self).post_install()

        # TODO: reinstall coreutils so ls displays extra acl bit
