# ( ͡° ͜ʖ ͡°)
import discord, os, chat

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)



@client.event
async def on_message(msg):
  if msg.content[:22] == '<@!' + str(client.user.id) + '>':
    await chat.respond(msg, msg.content[23:])
    


client.run(token)
