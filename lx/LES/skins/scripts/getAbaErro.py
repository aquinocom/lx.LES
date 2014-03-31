## Script (Python) "getAbaErro"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=errors
##title=Abas com erros

fields = errors.keys()
schematas = []
for field in fields:
    schemata = context.getField(field).schemata
    if not (schemata in schematas):
        schematas.append(schemata)
return schematas