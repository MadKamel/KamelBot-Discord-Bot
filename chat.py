import string, pickle

async def respond(msg, data, ctx):
  ctx_new = ctx

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))

  split = punc.split(' ')
  print(split)

  for i in range(len(split)):
    if split[i] in open("keywords/happy.emo").read():
      ctx_new[1] = ctx_new[1] + 1
    elif split[i] in open("keywords/sad.emo").read():
      ctx_new[1] = ctx_new[1] - 1

  print(str(ctx_new))
  await msg.channel.send(str(ctx_new))

  return ctx_new