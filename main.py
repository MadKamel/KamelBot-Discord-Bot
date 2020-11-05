# ( ͡° ͜ʖ ͡°)

import discord, os


# Init data
intents = discord.Intents.all()
token = os.getenv('token')

# Create discord Bot Client
client = discord.Client(intents=intents)


# Run discord Bot Client
client.run(token)
print("***| BreenBot is ready.")