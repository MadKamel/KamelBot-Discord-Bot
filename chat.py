import string, random

auto = True
training = False

async def respond(msg, data, ctx, client):
  global auto
  global training

  out = "<Unanticipated Input Error>"
  

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))
  split = punc.split(' ')

  if auto: print(punc)
  
  setin = open("set.in").read().split('\n')
  if auto: print(setin)

  setout = open("set.out").read().split('\n')
  if auto: print(setout)

  setrun = open("set.run").read().split('\n')
  if auto: print(setrun)

  setoutctx = open("setout.ctx").read().split('\n')
  if auto: print(setoutctx)

  setinctx = open("setin.ctx").read().split('\n')
  if auto: print(setinctx)

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

  else:
    if auto and training:
      open("zzz.imp", "+a").write(punc + '\n')
    
    else:
      out = input('(' + msg.author.name + ')\n' + punc + "\n\n >")
      if training:
        if not((punc in setin) and (out in setout)):
          open("set.in", "+a").write(punc + '\n')
          open("set.out", "+a").write(out + '\n')


  await msg.channel.send(out)
  if auto: print(out)
  return punc, out