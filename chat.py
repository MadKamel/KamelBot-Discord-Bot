import string

async def respond(msg, data, ctx):
  ctx_new = ctx

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))

  split = punc.split(' ')
  print(split)

  setin = open("set.in").read().split('\n')
  print(setin)

  setout = open("set.out").read().split('\n')
  print(setout)

  if split[0] in setin:
    out = setout[setin.index(split[0])]
    await msg.channel.send(out)
    print(out)

  return ctx_new