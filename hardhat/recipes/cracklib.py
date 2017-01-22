from .base import GnuRecipe
from string import Template


class Extra:
    pass


class CrackLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrackLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '17cf76943de272fd579ed831a1fd8533' \
                      '9b393f8d00bf9e0d17c91e972f583343'

        self.name = 'cracklib'
        self.version = '2.9.6'
        self.version_url = 'https://github.com/cracklib/cracklib/releases/'
        self.url = 'https://github.com/cracklib/cracklib/releases/download/' \
                   'cracklib-$version/cracklib-$version.tar.gz'
        self.configure_args += ['--with-default_dict=%s/lib/cracklib/pw_dict'
                                % self.prefix_dir]

        self.words = Extra()
        self.words.name = 'cracklib-words'
        self.words.version = self.version
        self.words.url = 'https://github.com/cracklib/cracklib/releases/' \
                         'download/cracklib-$version/' \
                         'cracklib-words-$version.gz'
        self.words.sha256 = '27973245225eeb9d0090e97f3dea4197' \
                            'dec99b64d9d3a791a60298f3b021824c'

        self.extra_downloads += [self.words]

    def install(self):
        super(CrackLibRecipe, self).install()
        self.log_dir('install', self.directory, 'installing cracklib words')
        script = Template(r''' "\
install -v -m644 -D  $file \
                         $prefix/share/dict/cracklib-words.gz     &&

gunzip -v                $prefix/share/dict/cracklib-words.gz     &&
ln -v -sf cracklib-words $prefix/share/dict/words                 &&
echo $$(hostname) >>      $prefix/share/dict/cracklib-extra-words  &&
install -v -m755 -d      $prefix/lib/cracklib                         &&

create-cracklib-dict     $prefix/share/dict/cracklib-words \
                         $prefix/share/dict/cracklib-extra-words"
''').substitute(prefix=self.prefix_dir,
                file=self.words.filename)

        args = self.shell_args + ['-c', script]
        self.run_exe(args, self.directory, self.environment)
