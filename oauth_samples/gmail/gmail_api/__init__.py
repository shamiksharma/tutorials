import imaplib
import string, email, re
from email.parser import HeaderParser

#-------------------------------------------------


class GAccount(object):
  
  def __init__(self, connection):
    self.server = connection
    self.mboxes = dict()
    self.messages = list()
    return

  def getMboxes(self):
    for mbox in self.server.list()[1]:
      name = mbox.split(' "/" ')[1][1:-1]
      print "Label: %s" % name
      if ( '[Gmail]' == name.strip() ): pass
      else: 
        self.mboxes[name] = GMbox(self,name)
    return self.mboxes

#-------------------------------------------------


class GMessage(object):

  def __init__(self):

    self.mboxName = None   # surprisingly id depends on mboxName
    self.id = None
    self.uid = None
    self.flags = None

    self.date = None
    self.From = None
    self.Subject = '( no subject )'
    self.Body = None

  def __repr__(self):
    str = "\nmessage={\nID: %s, \nUID: %s, \nFlags: %s, \nDate: %s," % (self.id,self.uid,self.flags,self.date)
    str += "\nFrom: %s, \nSubject: %s \n}" % (self.From,self.Subject)
    return str

#-------------------------------------------------

class GMbox(object):

  def __init__(self, account, name):
    self.account = account
    self.mboxName = name
    self.messages = list()
    self.loaded = False

  def getMessages (self, type=None, dates=(),  ):
    print "Num  #messages = %s" % len(self.messages)
    if not self.loaded :
      print "Not yet loaded"
      raise Error("Not yet loaded")
    return self.messages


  def __repr__(self):
    return "mailbox: {name: %s, num_messages:%d }" %  (self.mboxName, len(self.messages))


  def parseFlags(self, flags):
    return flags.split()  # Note that we don't remove the '\' from flags, just split by space

    
  def parseMetadata(self, entry):
    if(not getattr(self,'metadataExtracter',False) ):   #Lazy initiation of the parser
        self.metadataExtracter = re.compile(r'(?P<id>\d*) \(UID (?P<uid>\d*) FLAGS \((?P<flags>.*)\)\s')  
        #  I hate regexps.
        #  (\d*) = MSG ID,  the position index of the message in its mailbox
        #  \(UID (\d*) = MSG UID, the unique id of this message within its mailbox
        #  FLAGS \((.*)\)\s = MSG FLAGS, special indicators like (\Starred, \Seen) may be empty
        #  example:  55 (UID 82 FLAGS (\Seen) BODY[HEADER.FIELDS (SUBJECT FROM)] {65}
        #               groupdict() = { id:'55', uid:'82', flags:'\\Seen' }        
    metadata = self.metadataExtracter.match(entry).groupdict() 
    metadata['flags'] = self.parseFlags(metadata['flags'])
    return metadata
    
  def parseHeaders(self,entry):
    if(not getattr(self,'headerParser',False) ):
        self.headerParser = HeaderParser()  #See http://docs.python.org/library/email.parser.html#parser-class-api    
    headers = self.headerParser.parsestr(entry)
    return headers

  def process(self):

    server = self.account.server
    mboxName = self.mboxName
  
    result, message = server.select(mboxName,readonly=1)
    if result != 'OK':
        raise Exception, message
    
    typ, data = server.search(None, '(UNDELETED)')
    fetch_list = string.split(data[0])[-10:]
    # limit to N most recent messages in mailbox, this is where pagination should be implemented
    fetch_list = ','.join(fetch_list)
    
    if(fetch_list):
      f = server.fetch(fetch_list, '(UID FLAGS BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])')
      for fm in f[1]:
        if(len(fm)>1):
          metadata = self.parseMetadata(fm[0]) #metadata is contained 
          headers = self.parseHeaders(fm[1])
          
          message = GMessage()
          message.id = metadata['id']
          message.uid = metadata['uid']
          message.flags = metadata['flags']
          message.mailbox = mboxName   #UID depends on mailbox location so,
                                      #we need to know which owns the message

          message.date = headers['Date']
          message.From = headers['From']
          if( 'Subject' in headers ):
              message.Subject = headers['Subject']
              
          self.messages.append(message)

    self.loaded = True
    print "Num messages = %s" % len(self.messages)

  def getMessage (self, uid):
    self.account.server.select(self.mboxName)
    status, data = self.server.uid('fetch',uid, 'RFC822')
    
    messagePlainText = ''
    messageHTML = ''

    for response_part in data:
      if isinstance(response_part, tuple):
        msg = email.message_from_string(response_part[1])
        for part in msg.walk():
          if str(part.get_content_type()) == 'text/plain':
            messagePlainText = messagePlainText + str(part.get_payload())
          if str(part.get_content_type()) == 'text/html':
            messageHTML = messageHTML + str(part.get_payload())


    #create new message object
    message = GMessage()
    
    if(messageHTML != '' ):
        message.Body = messageHTML
    else:
        message.Body = messagePlainText
    if('Subject' in msg):
        message.Subject = msg['Subject']
    message.From = msg['From']
    
    message.uid = uid
    message.mboxName = self.mboxName
    message.date = msg['Date']
    return message



#------------------------------------------------------





#------------------------------------------------------

