import string, pickle

async def respond(msg, data, ctx):
  ctx_new = ctx

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))

  split = punc.split(' ')
  print(split)



  return ctx_new