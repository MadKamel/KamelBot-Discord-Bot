import string, random, natlang

auto = True
training = False
debug = False

async def respond(msg, data, ctx, client):
  global auto
  global training
  global debug

  out = "<Unanticipated Input Error>"
  

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))
  split = punc.split(' ')

  if auto and debug: print(punc)
  
  setin = open("set.in").read().split('\n')
  if auto and debug: print(setin)

  setout = open("set.out").read().split('\n')
  if auto and debug: print(setout)

  setrun = open("set.run").read().split('\n')
  if auto and debug: print(setrun)

  topics = open("set.tpc").read().split('\n')
  if auto and debug: print(topics)

  if (punc in setin) and auto:
    prob = []
    for i in range(len(setin)):
      if setin[i] == punc:
        prob.append(i)
    out = setout[random.choice(prob)]
    #out = setout[setin.index(punc)]

    if out == '*':
      out = setrun[setin.index(punc)]
      spl = out.split('|')
      for i in range(len(spl)):
        if i/2 != int(i/2):
          spl[i] = client.get_user(int(spl[i])).mention
      out = ''.join(spl)

    elif out == '.':
      out = random.choice(topics)

    elif out == '?':
      out = 'Oh, I thought that made sense in my head, sorry!'

  else:

    if auto:
      out = natlang.parse(punc)
    
    else:
      out = input('(' + msg.author.name + ')\n' + punc + "\n\n >")
      if training:
        if not((punc in setin) and (out in setout)):
          if not out == '#':
            open("set.in", "+a").write(punc + '\n')
            open("set.out", "+a").write(out + '\n')


  await msg.channel.send(out)
  if auto and debug: print(out)
  return punc, out