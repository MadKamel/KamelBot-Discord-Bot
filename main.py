# ( ͡° ͜ʖ ͡°)
import discord, os, chat, irc, comms, threading
os.system('clear')

open('dis.syn', 'w').write('nul')
open('irc.syn', 'w').write('nul')


channel = "#mk-comms"
server = "irc.freenode.net"
nickname = "mk-comms-agent01"

ircclient = irc.IRC()
ircclient.connect(server, channel, nickname)


intents = discord.Intents.all()
token = os.getenv('token')
client = discord.Client(intents=intents)


ctx = ['', '']



@client.event
async def on_message(msg):
  global ctx
  if msg.content[:22] == '<@!' + str(client.user.id) + '>':
    ctx = await chat.respond(msg, msg.content[23:], ctx, client)
  elif msg.content[0] == '$':
    print(msg.content)
    open('irc.syn', 'w').write(msg.content[1:])
  else:
    pass
    


def ircDaemonRoutine():
  print('irc daemon 1 running')
  global ircclient
  global channel
  global nickname
  while True:
    cmd, user, fullmsg = comms.parsecmd(ircclient.get_text())
    if not cmd == None:
      if cmd == 'ping':
        ircclient.send(channel, 'pong')
        print('ping from ' + user + ' ponged.')

      elif cmd == 'pong':
        print('pong from ' + user + ' recieved.')

      elif cmd == 'send':
        if fullmsg.split(' ')[1] == nickname:
          print('sending message from ' + user + ' to #general.')
          open('dis.syn', 'w').write(' '.join(fullmsg.split(' ')[2:]))
    

def ircDaemonRoutine2():
  print('irc daemon 2 running')
  global ircclient
  global channel
  while True:
    int_cmd = open('irc.syn').read()
    if not int_cmd == 'nul':
      print(int_cmd)
      ircclient.send(channel, int_cmd)
      open('irc.syn', 'w').write('nul')


async def disDaemonRoutine():
  print('discord daemon running')
  global client
  homechannel = client.get_channel(772960791674355762)
  while True:
    send_msg_todiscord = open('dis.syn').read()
    if not send_msg_todiscord == 'nul':
      print(send_msg_todiscord)
      yield homechannel.send(open('dis.syn').read())
      open('dis.syn', 'w').write('nul')



ircDaemon = threading.Thread(target=ircDaemonRoutine, daemon=True)
ircDaemon.start()

ircDaemon2 = threading.Thread(target=ircDaemonRoutine2, daemon=True)
ircDaemon2.start()

disDaemon = threading.Thread(target=disDaemonRoutine, daemon=True)
disDaemon.start()


print('KamelBot going online.')
client.run(token)