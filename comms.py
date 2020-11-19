def parsecmd(msg):
  cmd = None
  user = None
  spl = msg.split(' ')
  if spl[1] == 'PRIVMSG':
    user = spl[0][1:].split('!')[0]
    cmd = spl[3][1:].split('\r\n')[0]
  
  return cmd, user, ' '.join(spl[3:])[1:]
