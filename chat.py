import string

async def respond(msg, data, ctx):
  ctx_new = ctx

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))
  split = punc.split(' ')

  print(punc)
  
  setin = open("set.in").read().split('\n')
  print(setin)

  setout = open("set.out").read().split('\n')
  print(setout)

  if punc in setin:
    out = setout[setin.index(punc)]
  else:
    open("zzz.imp", "+a").write(punc)


  await msg.channel.send(out)
  print(out)
  return ctx_new