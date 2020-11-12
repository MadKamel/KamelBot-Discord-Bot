import string

async def respond(msg, data, ctx):

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))

  split = punc.split(' ')
  print(split)