# ( ͡° ͜ʖ ͡°)
import discord, os, chat, chatterbot

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)

chatbot = chatterbot.ChatBot('Export Example Bot')
chatbot.trainer.export_for_training('./export.yml')

ctx = None



@client.event
async def on_message(msg):
  global ctx
  if msg.content[:22] == '<@!' + str(client.user.id) + '>':
    ctx = await chat.respond(msg, msg.content[23:], ctx)
    


client.run(token)
