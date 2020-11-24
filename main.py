# ( ͡° ͜ʖ ͡°)
import discord, os
os.system('clear')

intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)



@client.event
async def on_ready():
  global InfoSecLogs
  InfoSecLogs = loadchan(780619821720141904)


@client.event
async def on_message(msg):
  print('@' + msg.author.name + ' #' + msg.channel + ' =' + msg.content)


@client.event
async def on_invite_create(invite):
  ISLog(0, invite.inviter.mention)





# Load Channel function
def loadchan(id): # Loads a channel
  global client
  print('Channel #' + str(client.get_channel(id)) + ' loaded.')
  return client.get_channel(id)

def loadrole(guild, id): # Loads a role from a specific guild
  print('Role <' + str(guild.get_role(id)) + '> loaded.')
  return guild.get_role(id)

def loadguild(id): # Loads a guild (server)
  global client
  print('Guild ' + str(client.get_guild(id)) + ' loaded.')
  return client.get_guild(id)

def loadmember(guild, id): # Loads a member from an id
  print('User @' + str(guild.get_member(id)) + ' loaded.')
  return guild.get_member(id)

async def setstatus(activity):
  global client
  print('Setting status to: ' + activity)
  await client.change_presence(status=discord.Status.online, activity=discord.Game(activity))

  

# IS Log Types/Severities
IS_severity = []
IS_codes = []


IS_severity.append('HIGH')
IS_codes.append('invite link created')



async def ISLog(code, details):
  global InfoSecLogs

  await InfoSecLogs.send('@here\nURGENCY: ' + IS_severity[code] + '\nACTIVITY: ' + IS_codes[code] + '\nDETAILS: ' + details)

print('KamelBot going online.')
client.run(token)
