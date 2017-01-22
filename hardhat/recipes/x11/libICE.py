from .base import X11BaseRecipe


class LibICERecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibICERecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8f7032f2c1c64352b5423f6b48a8ebdc' \
                      '339cc63064af34d66a6c9aa79759e202'

        self.name = 'libICE'
        self.version = '1.0.9'
        self.depends = ['xorg-headers', 'xtrans']
