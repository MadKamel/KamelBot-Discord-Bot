def parse(msg):
  worker = ''
  msg_split = msg.split(' ')
  
  patterns = open('vocab/patterns.grm').read().split('\n')

  noun = open('vocab/noun.voc').read().split('\n')

  nouns = open('vocab/nouns.voc').read().split('\n')

  adjective = open('vocab/adjective.voc').read().split('\n')

  verb = open('vocab/verb.voc').read().split('\n')

  msg_translated = []
  for i in range(len(msg_split)):
    if msg_split[i] in noun:
      msg_translated.append("'noun'")
    elif msg_split[i] in nouns:
      msg_translated.append("'nouns'")
    elif msg_split[i] in adjective:
      msg_translated.append("'adjective'")
    elif msg_split[i] in verb:
      msg_translated.append("'verb'")
    else:
      msg_translated.append(msg_split[i])
  
  msg_translated = ' '.join(msg_translated)
  
  for i in range(len(patterns)):
    if patterns[i] == msg_translated:
      # this pattern will apply.
      worker = patterns[i]
      print(worker)

  return msg_translated, worker