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
  print('\nINCOMING:===============\n@ ' + msg.author.name + '\n# ' + msg.channel.name + '\n= ' + msg.content + '\n========================\n')


@client.event
async def on_invite_create(invite):
  await ISLog(0, invite.inviter.mention)


@client.event
async def on_invite_delete(invite):
  await ISLog(1)





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
IS_codes = []


IS_codes.append('Invite Link Generated.')
IS_codes.append('Invite Link Deleted.')
IS_codes.append('New Member Joined.')




async def ISLog(code, details="Nothing provided."):
  global InfoSecLogs

  await InfoSecLogs.send('Attention, @here:\nACTION CODE: **' + str(code) + '**\nACTIVITY: ' + IS_codes[code] + '\nDETAILS: ' + details)
  print('\nINCIDENT:\n=======================\n| ACTION CODE: **' + str(code) + '**\n| ACTIVITY: ' + IS_codes[code] + '\n| DETAILS: ' + details + '\n\n')

print('KamelBot going online.')
client.run(token)