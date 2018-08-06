from .base import X11AppBaseRecipe, X11BaseRecipe


classes = [('bdftopcf', '1.1', '4b4df05fc53f1e98993638d6f7e178d9'
                               '5b31745c4568cee407e167491fd311a2'),
           ('iceauth', '1.0.7', '1216af2dee99b318fcf8bf9a25991527'
                                '3bcb37a7f1e7859af4f15d0ebf6f3f0a'),
           ('luit', '1.1.1', '30b0e787cb07a0f504b70f1d61239305'
                             '22111ce9d4276f6683a69b322b49c636'),
           ('mkfontdir', '1.0.7', '56d52a482df130484e51fd066d1b6eda'
                                  '7c2c02ddbc91fe6e2be1b9c4e7306530'),
           ('mkfontscale', '1.1.2', '8c6d5228af885477b9aec60ca6f17257'
                                    '8e7d2de42234357af62fb00439453f20'),
           ('sessreg', '1.1.0', '551177657835e0902b5eee7b19713035'
                                'beaa1581bbd3c6506baa553e751e017c'),
           ('setxkbmap', '1.3.1', 'a9ddb3963f263ba13f0ea105d8c45a53'
                                  '1832140530217cc559587bb94f02d3e1'),
           ('smproxy', '1.0.6', '6cf19155a2752237f36dbf8bc4184465'
                                'ea190d2652f887faccb4e2a6ebf77266'),
           ('x11perf', '1.6.0', 'e87098dec1947572d70c62697a7b70bd'
                                'e1ab5668237d4660080eade6bc096751'),
           ('xauth', '1.0.9', '56ce1523eb48b1f8a4f4244fe1c3d8e6'
                              'af1a3b7d4b0e6063582421b0b68dc28f'),
           ('xcmsdb', '1.0.5', 'e5585361bb8b6a05bb814a8d0e444ee9'
                               '3e0f00180881d3070aff4571e97f67c6'),
           ('xcursorgen', '1.0.6', '31c8910f54eb175a8a74a60e76626974'
                                   '67e21a8bf948220a6048a93924b3f66c'),
           ('xdpyinfo', '1.3.2', '30238ed915619e06ceb41721e5f747d6'
                                 '7320555cc38d459e954839c189ccaf51'),
           ('xdriinfo', '1.0.5', '4cba3766ef89557422062287248adeb9'
                                 '33999071bad6f3ef9c0a478a3c680119'),
           ('xev', '1.2.2', 'd94ae62a6c1af56c2961d71f5782076a'
                            'c4116f0fa4e401420ac7e0db33dc314f'),
           ('xgamma', '1.0.6', '0ef1c35b5c18b1b22317f455c8df13c0'
                               'a471a8efad63c89c98ae3ce8c2b222d3'),
           ('xhost', '1.0.7', '93e619ee15471f576cfb30c663e18f5b'
                              'c70aca577a63d2c2c03f006a7837c29a'),
           ('xinput', '1.6.2', '3694d29b4180952fbf13c6d4e5954131'
                               '0cbb11eef5bf888ff3d8b7f4e3aee5c4'),
           ('xkbcomp', '1.3.1', '0304dc9e0d4ac10831a9ef5d54197223'
                                '75ddbc3eac3ff4413094d57bc1f1923d'),
           ('xkbevd', '1.1.4', '2430a2e5302a4cb4a5530c1df8cb3721'
                               'a149bbf8eb377a2898921a145197f96a'),
           ('xkbutils', '1.0.4', 'd2a18ab90275e8bca028773c44264d22'
                                 '66dab70853db4321bdbc18da75148130'),
           ('xkill', '1.0.4', '88ef2a304f32f24b255e879f03c1dcd3'
                              'a2be3e71d5562205414f267d919f812e'),
           ('xlsatoms', '1.1.2', '47e5dc7c3dbda6db2cf8c00cedac1722'
                                 '835c1550aa21cfdbc9ba83906694dea4'),
           ('xlsclients', '1.1.3', '5d9666fcc6c3de210fc70d5a841a4049'
                                   '55af709a616fde530fe4e8f7723e3d3d'),
           ('xmessage', '1.0.4', 'bcdf4b461c439bb3ade6e1e41c47d621'
                                 '8b912da8e9396b7ad70856db2f95ab68'),
           ('xmodmap', '1.0.9', 'b7b0e5cc5f10d0fb6d2d6ea4f00c77e8'
                                'ac0e847cc5a73be94cd86139ac4ac478'),
           ('xpr', '1.0.4', 'fed98df31eb93d3dca4688cb535aabad'
                            '06be572e70ace3b1685679c18dd86cb5'),
           ('xprop', '1.2.2', '9bee88b1025865ad121f72d32576dd30'
                              '27af1446774aa8300cce3c261d869bc6'),
           ('xrandr', '1.5.0', 'c1cfd4e1d4d708c031d60801e527abc9'
                               'b6d34b85f2ffa2cadd21f75ff38151cd'),
           ('xrdb', '1.1.0', '73827b6bbfc9d27ca287d95a1224c306'
                             'd7053cd7b8156641698d7dc541ca565b'),
           ('xrefresh', '1.0.5', '3213671b0a8a9d1e8d1d5d9e3fd86842'
                                 'c894dd9acc1be2560eda50bc1fb791d6'),
           ('xset', '1.2.3', '4382f4fb29b88647e13f3b4bc2926313'
                             '4270747fc159cfc5f7e3af23588c8063'),
           ('xsetroot', '1.1.1', 'ba215daaa78c415fce11b9e58c365d03'
                                 'bb602eaa5ea916578d76861a468cc3d9'),
           ('xvinfo', '1.1.3', '9fba8b68daf53863e66d5004fa9c703f'
                               'cecf69db4d151ea2d3d885d621e6e5eb'),
           ('xwd', '1.0.6', '3bb396a2268d78de4b1c3e5237a85f78'
                            '49d3434e87b3cd1f4d57eef614227d79'),
           ('xwininfo', '1.1.3', '218eb0ea95bd8de7903dfaa26423820c'
                                 '523ad1598be0751d2d8b6a2c23b23ff8'),
           ('xwud', '1.0.4', 'd6b3a09ccfe750868e26bd2384900ab5'
                             'ff0d434f7f40cd272a50eda8aaa1f8bd')
           ]


def class_init(self, *args, **kwargs):
    X11AppBaseRecipe.__init__(self, *args, **kwargs)


def make_class(x):
    name = x[0]
    name = name[0].upper() + name[1:] + 'Recipe'
    return type(name,
                (X11AppBaseRecipe,),
                {'name': x[0], 'version': x[1], 'sha256': x[2],
                 '__init__': class_init})

APPS = [make_class(x) for x in classes]


class XBacklight(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(XBacklight, self).__init__(*args, **kwargs)
        self.name = 'xbacklight'
        self.version = '1.2.1'
        self.depends = ['xrandr']
        self.sha256 = '17f6cf51a35eaa918abec36b7871d28b' \
                      '712c169312e22a0eaf1ffe8d6468362b'
        self.url = 'http://ftp.x.org/pub/individual/app/' \
                   '$name-$version.tar.bz2'
        self.depends = ['libpng', 'mesa', 'xbitmaps', 'xcb-util']


APPS += [XBacklight]
