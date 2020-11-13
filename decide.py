def decide(noun, attribute, anstype):
  objects = open('knowledge/objects.att').read().split('\n')
  pointers = open('knowledge/objects.pnt').read().split('\n')

  if anstype == 1:
    attrs = open('knowledge/attributes.att').read().split('\n')

  elif anstype == 2:
    attrs = open('knowledge/actions.att').read().split('\n')


  attrlist = attrs[int(pointers[int(objects.index(noun))])].split('|')
  
  return attribute in attrlist