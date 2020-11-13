import decide

def parse(msg):
  worker = 0
  worker_type = 0
  working_noun = ''
  working_attr = ''

  msg_split = msg.split(' ')
  
  question_patterns = open('vocab/questions.grm').read().split('\n')

  declaration_patterns = open('vocab/declarations.grm').read().split('\n')

  noun = open('vocab/noun.voc').read().split('\n')

  adjective = open('vocab/adjective.voc').read().split('\n')

  verb = open('vocab/verb.voc').read().split('\n')

  msg_translated = []
  for i in range(len(msg_split)):
    if msg_split[i] in noun:
      msg_translated.append("'noun'")
    elif msg_split[i] in adjective:
      msg_translated.append("'adjective'")
    elif msg_split[i] in verb:
      msg_translated.append("'verb'")
    else:
      msg_translated.append(msg_split[i])
  
  msg_translated = ' '.join(msg_translated)
  
  for i in range(len(question_patterns)):
    if question_patterns[i] == msg_translated:
      worker_type = 1
      if i == 0 or i == 1:
        worker = 1
        working_noun = msg_split[1]
        working_attr = msg_split[2]
        break

      elif i == 2:
        worker = 2
        working_noun = msg_split[1]
        working_attr = msg_split[2]
        break

  if worker != 0:
    if worker_type = 1:
      return decide.decide(working_noun, working_attr, worker)
  else:
    return msg_translated