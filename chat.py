import string

async def respond(ctx, data):

  lower = data.lower()
  punc = lower.translate(str.maketrans('', '', string.punctuation))

  split = punc.split(' ')