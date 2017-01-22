try:
    from functools import cmp_to_key
except:  # python < 2.7
    from .cmp_to_key import cmp_to_key
import os
import re
from .urls import Urls
from .util import read_url
try:
    from urllib.parse import urlparse
except:
    # python 2
    from urlparse import urlparse


extension_regex = r'\.(?P<extension>(tar)|(tgz)|(zip)|' \
                   '(xz)|(tar\.bz2)|(tar\.gz)|(tar\.xz))'


def int_prefix(x):
    i = 0
    while i < len(x):
        try:
            y = int(x[i])
        except:
            break
        i += 1


    int_part = int(x[:i]) if i else 0
    non_int = x[i:]
    return (int_part, non_int)


def version_compare(xo, yo):
    x = xo.split('.')
    y = yo.split('.')

    min_len = min(len(x), len(y))
    for i in range(min_len):
        xi, xa = int_prefix(x[i])
        yi, ya = int_prefix(y[i])

        if xi < yi:
            return -1
        if xi > yi:
            return 1
        if xa and ya:
            if xa < ya:
                return -1
            if xa > ya:
                return 1
        if xa:
            if xa.startswith('rc') or xa.startswith('-rc'):
                return -1
            else:
                return 1
        if ya:
            if ya.startswith('rc') or ya.startswith('-rc'):
                return 1
            else:
                return -1
    if len(x) > len(y):
        return 1
    if len(x) < len(y):
        return -1
    return 0


class Versions:
    @staticmethod
    def max(versions):
        v = Versions.sort(versions)
        return v[-1] if len(v) else None

    @staticmethod
    def sort(versions):
        return sorted(versions, key=cmp_to_key(version_compare))

    @staticmethod
    def default_regex(name):
        return name + r'\-(?P<version>\d+\.\d+(\.\d+)?)' \
            + extension_regex

    @staticmethod
    def get_from_directory(url,
                           version_regex=None,
                           get_version_from_file=None):
        try:
            from bs4 import BeautifulSoup
        except:
            print('BeautifulSoup not installed for version checking')
            return (None, None)
        html = read_url(url)
        html = html.decode('utf-8', 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        hrefs = [n.get('href') for n in links]
        hrefs = [get_file(n) for n in hrefs]
        hrefs = list(filter(lambda s: isinstance(s, str), hrefs))
        if version_regex:
            hrefs = [re.match(version_regex, n) for n in hrefs]
        elif get_version_from_file:
            hrefs = [get_version_from_file(x) for x in hrefs]
        hrefs = list(filter(lambda x: x, hrefs))
        versions = [x.group('version') for x in hrefs]
        version = Versions.max(versions)
        return (version, len(set(versions)) > 1)

    @staticmethod
    def scrape_page(url, version_regex):
        html = read_url(url)
        html = html.decode('utf-8', 'ignore')
        matches = re.finditer(version_regex, html)
        versions = [x.group('version') for x in matches]
        versions = list(filter(lambda x: x, versions))
        return (Versions.max(versions), len(set(versions)) > 1)

    @staticmethod
    def get_from_directory_version(url,
                                   version_regex=None,
                                   get_version_from_file=None):
        url = Urls.drop_file(url)
        return Versions.get_from_directory(url, version_regex,
                                           get_version_from_file)


def get_file(url):
    p = urlparse(url)
    x = os.path.basename(p.path)
    return x if x else p.path


if __name__ == '__main__':
    url = 'http://cran.mtu.edu/src/base/R-3/R-3.3.2.tar.gz'
    versions = Versions.get_from_directory_version(
        url, r'R\-(?P<version>.+).tar.gz')
    print(versions)
