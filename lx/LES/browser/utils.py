# -*- coding: utf-8 -*-

#Methods


def getFields(self, schemata):
    """Retorna todos os campos do schemata
    """
    not_visible = ['id', 'title', 'description']
    default_fields = []
    fields = self.context.Schemata()[schemata].fields()
    for field in fields:
        if not (field.getName() in not_visible):
            default_fields.append(field)
    return default_fields
