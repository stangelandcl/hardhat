from .base import PipBaseRecipe


class JsonSchemaRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(JsonSchemaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '36673ac378feed3daa5956276a829699' \
                      '056523d7961027911f064b52255ead41'

        self.name = 'jsonschema'
        self.version = '2.5.1'
