def parsecmd(msg):
  cmd = None
  user = None
  spl = msg.split(' ')
  if spl[1] == 'PRIVMSG':
    user = spl[0][1:].split('!')[0]
    cmd = spl[3][1:].split('\r\n')[0]
  
  return cmd, user

def format_msg(msg):
  outgoing = []
  outgoing.append('discordMsg')
  outgoing.append(msg.content)
  outgoing.append(msg.author.name)
  outgoing.append(msg.channel.name)
  return '|'.join(outgoing)


def format_packet(packet):
  parse = packet.split('|')
  return parse