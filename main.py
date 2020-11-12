# ( ͡° ͜ʖ ͡°)
import discord, os, chat


intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)


# Emotional states
#   p0: ?
#   p1: ?
#   p2: ?

ctx = [0, 0, 0]



@client.event
async def on_message(msg):
  global ctx
  if msg.content[:22] == '<@!' + str(client.user.id) + '>':
    ctx = await chat.respond(msg, msg.content[23:], ctx)
    


client.run(token)
