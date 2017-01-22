import os
from string import Template
from .base import GnuRecipe


class DocbookXmlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DocbookXmlRecipe, self).__init__(*args, **kwargs)
        self.name = 'docbook-xml'
        self.version = ''

    def run(self):
        versions = [
            ('4.3', '23068a94ea6fd484b004c5a73ec36a66'
                    'aa47ea8f0d6b62cc1695931f5c143464'),
            ('4.5', '4e4e037a2b83c98c6c94818390d4bdd3'
                    'f6e10f6ec62dd79188594e26190dc7b4')
            ]
        for version, hash in versions:
            x = DocbookXml(settings=self)
            x.version = version
            x.sha256 = hash
            x.name = x.name + x.version
            self.log_dir('install', self.directory,
                         'installing version %s' % x.version)
            x.clean()
            x.run()

    def version_check(self):
        pass


class DocbookXml(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DocbookXml, self).__init__(*args, **kwargs)
        self.name = 'docbook-xml'
        self.depends = ['docbook-xsl', 'sgml-common']
        self.url = 'http://www.docbook.org/xml/$version/docbook-xml-$version.zip'

    def extract(self):
        self.log_dir('extract', self.directory, 'extracting')

        self.extract_args = ['unzip', self.filename, '-d', self.directory]
        self.run_exe(self.extract_args, self.tarball_dir, self.environment)

    def version_check(self):
        pass

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing and xmlcatalog')
        text = Template(r'''
install -d ${prefix}/share/xml/docbook/xml-dtd-${version} &&
cp -af docbook.cat *.dtd ent/ *.mod \
    ${prefix}/share/xml/docbook/xml-dtd-${version} &&
if [ ! -e ${prefix}/etc/xml/catalog ]; then mkdir -p ${prefix}/etc/xml; xmlcatalog \
    --noout --create ${prefix}/etc/xml/catalog; fi &&
if [ ! -e ${prefix}/etc/xml/docbook ]; then xmlcatalog --noout --create \
    ${prefix}/etc/xml/docbook; fi &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Information Pool V${version}//EN" \
        "file://${prefix}/share/xml/docbook/xml-dtd-${version}/dbpoolx.mod" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML V${version}//EN" \
    "http://www.oasis-open.org/docbook/xml/${version}/docbookx.dtd" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Character Entities V${version}//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/dbcentx.mod" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Notations V${version}//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/dbnotnx.mod" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ENTITIES DocBook XML Additional General Entities V${version}//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/dbgenent.mod" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//ELEMENTS DocBook XML Document Hierarchy V${version}//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/dbhierx.mod" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/soextblx.dtd" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "public" \
    "-//OASIS//DTD DocBook XML CALS Table Model V${version}//EN" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}/calstblx.dtd" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "rewriteSystem" \
    "http://www.oasis-open.org/docbook/xml/${version}" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "rewriteURI" \
    "http://www.oasis-open.org/docbook/xml/${version}" \
    "file://${prefix}/share/xml/docbook/xml-dtd-${version}" \
    ${prefix}/etc/xml/docbook &&
xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//ENTITIES DocBook XML" \
    "file://${prefix}/etc/xml/docbook" ${prefix}/etc/xml/catalog &&
xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//DTD DocBook XML" \
    "file://${prefix}/etc/xml/docbook" ${prefix}/etc/xml/catalog &&
xmlcatalog --noout --add "delegateSystem" \
    "http://www.oasis-open.org/docbook/" \
    "file://${prefix}/etc/xml/docbook" ${prefix}/etc/xml/catalog &&
xmlcatalog --noout --add "delegateURI" \
    "http://www.oasis-open.org/docbook/" \
    "file://${prefix}/etc/xml/docbook" ${prefix}/etc/xml/catalog
''')

        text = text.substitute(prefix=self.prefix_dir,
                               version=self.version)
        self.run_exe(text, self.directory, self.environment)
