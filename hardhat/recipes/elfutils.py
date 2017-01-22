from .base import GnuRecipe


class ElfUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ElfUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3c056914c8a438b210be0d790463b960' \
                      'fc79d234c3f05ce707cbff80e94cba30'

        self.name = 'elfutils'
        self.version = '0.166'
        self.depends = ['valgrind']
        self.url = 'https://fedorahosted.org/releases/e/l/elfutils/' \
                   '$version/elfutils-$version.tar.bz2'

        self.environment['CFLAGS'] += ' -Wno-error=maybe-uninitialized' \
            ' -Wno-error=unused-but-set-variable -Wno-error=unused-variable' \
            ' -Wno-error=null-dereference'
        self.environment_strip_lto()

        # From linux from scratch. Avoids conflicts with binutils patches
        self.configure_args += ['--program-prefix="eu-"']
