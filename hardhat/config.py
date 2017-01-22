try:
    from io import StringIO
except ImportError:
    from CStringIO import StringIO
try:
    from configparser import RawConfigParser, ConfigParser
except ImportError:
    from ConfigParser import RawConfigParser, ConfigParser


def getdefault(parser, section, option, default=None):
    if not parser.has_option(section, option):
        return default
    return parser.get(section, option)


def getdefaultfloat(parser, section, option, default=None):
    return getdefault(parser, section, option, default)


def getdefaultint(parser, section, option, default=None):
    return getdefault(parser, section, option, default)


def read_config(filename, root_section=None):
    with open(filename, 'rt') as f:
        text = f.read()

    if root_section:
        text = '[%s]\n%s' % (root_section, text)

    fp = StringIO(text)
    parser = RawConfigParser()
    p = parser.readfp(fp)
    p.getdefault = getdefault
    p.getdefaultint = getdefaultint
    p.getdefaultfloat = getdefaultfloat
    return p


def read_file_list(filename):
    # one package per line.
    # # is a comment
    with open(filename, 'rt') as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    lines = list(filter(lambda x: len(x) >= 1 and not x.startswith('#'),
                        lines))

    for i in range(len(lines)):
        line = lines[i].strip()
        for j in range(len(line)):
            if line[j] == '#':
                line = line[:j]
                break
        lines[i] = line

    return lines
