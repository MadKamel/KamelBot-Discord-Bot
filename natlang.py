import re

def parse(msg):
  worker = ''
  msg_split = msg.split(' ')
  
  patterns = open('vocab/patterns.grm').read().split('\n')

  noun = open('vocab/noun.voc').read().split('\n')


  msg_translated = []
  for i in range(len(msg_split)):
    if msg_split[i] in noun:
      msg_translated.append("'noun'")
    elif msg_split[i] in noun:
      msg_translated.append("'adjective'")
    else:
      msg_translated.append(msg_split[i])
  
  
  for i in range(len(patterns)):
    if patterns[i] == msg_translated:
      # this pattern will apply.
      worker = patterns[i]

  return msg_translated, worker