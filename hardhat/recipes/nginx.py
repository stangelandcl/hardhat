from .base import GnuRecipe


class NginxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ed647c3dd65bc4ced03b0e0f6bf9e63' \
                      '3eff6b01bac772bcf97077d58bc2be4d'

        self.name = 'nginx'
        self.version = '1.10.0'
        self.url = 'http://nginx.org/download/nginx-$version.tar.gz'
        self.configure_strip_cross_compile()
