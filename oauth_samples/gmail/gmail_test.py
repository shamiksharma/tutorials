
import settings
import sys
import urlparse
import time
import getopt
import pickle
import os
import webbrowser

sys.path.append("..") # so you can import the ../oauth2 lib
import oauth2 as oauth
import oauth2.clients.imap as imaplib

consumer_key = settings.consumer_key
consumer_secret = settings.consumer_secret

request_token_url = settings.request_token_url
access_token_url = settings.access_token_url
authorize_url = settings.authorize_url

#-------------------------------------------

def oauth_gen_request_token():
  print consumer_key, consumer_secret
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  client = oauth.Client(consumer)

  # Step 1: Get a request token. This is a temporary token that is used for 
  # having the user authorize an access token and to sign the request to obtain 
  # said access token.

  print request_token_url
  
  resp, content = client.request(request_token_url, "GET", {'scope':'https://mail.google.com/', 'oauth_callback' : 'oob'})

  if resp['status'] != '200':
      raise Exception("Invalid response %s." % resp['status'])

  request_token = dict(urlparse.parse_qsl(content))

  print "Request Token:"
  print "    --oauth_token=%s" % request_token['oauth_token']
  print "    --oauth_token_secret=%s" % request_token['oauth_token_secret']
  print 

  # Step 2: Redirect to the provider. Since this is a CLI script we do not 
  # redirect. In a web application you would redirect the user to the URL
  # below.
  import urllib
  auth_url = "%s?oauth_token=%s" % (authorize_url, urllib.quote(request_token['oauth_token'],'') )

  print "Going to the following link in your browser:"
  print auth_url

  webbrowser.open_new(auth_url)

  # After the user has granted access to you, the consumer, the provider will
  # redirect you to whatever URL you have told them to redirect to. You can 
  # usually define this in the oauth_callback argument as well.
  accepted = 'n'
  while accepted.lower() == 'n':
      accepted = raw_input('Have you authorized me? (y/n) ')
  oauth_verifier = raw_input('What is the PIN? ')

  # Step 3: Once the consumer has redirected the user back to the oauth_callback
  # URL you can request the access token the user has approved. You use the 
  # request token to sign this request. After this is done you throw away the
  # request token and use the access token returned. You should store this 
  # access token somewhere safe, like a database, for future use.
  
  token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
  token.set_verifier(oauth_verifier.strip())
  return token

#-------------------------------------------

def oauth_gen_access_token(request_token):
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  client = oauth.Client(consumer, request_token)
  resp, content = client.request(access_token_url, "GET")
  access_token = dict(urlparse.parse_qsl(content))

  print "Access Token:"
  print "    --oauth_token= %s" % access_token['oauth_token']
  print "    --oauth_token_secret=%s" % access_token['oauth_token_secret']
  print
  print "You may now access protected resources using the access tokens above." 
  print
  return access_token

#-------------------------------------------


def oauth_request(url, token_key, token_secret, app_key, app_secret):
  # Set up instances of our Token and Consumer. The Consumer.key and 
  # Consumer.secret are given to you by the API provider. The Token.key and
  # Token.secret is given to you after a three-legged authentication.
  token = oauth.Token(key=token_key, secret=token_secret)
  consumer = oauth.Consumer(key=app_key, secret=app_secret)
  client = oauth.Client(consumer,token)
  resp, content = client.request(
          url,
          method="GET",
          body='',
          headers=None
      )
  return content

#-------------------------------------------

def print_usage(cmd, msg):
  print >>sys.stderr, "Usage: %s -u [user_email_address]" % cmd
  return 


def main(argv=None):
  
  if argv is None:  argv = sys.argv
  cmd = argv[0]
  
  try:
    opts, args = getopt.getopt(argv[1:], "u:", ["user="])
  except getopt.GetoptError, msg:
    print_usage(cmd, msg)
    return 2

  user_email_address = None
  for o,a in opts:
    if o in ("-u", "--user"):
      user_email_address = a

  if user_email_address is None:
    print_usage(cmd, "No email address provided")
    return 2


  token_file_path = settings.token_file_path
  have_token = False;

  # Check if we already have a token saved in the filesystem

  if not os.path.exists(token_file_path):
    app_authorized_token = oauth_gen_request_token()
    access_token = oauth_gen_access_token(app_authorized_token)
    token = access_token

    pickle.dump( token, open(token_file_path,"wb"))
  else:
    print 'Found existing tokens'
  
  token = pickle.load( open(token_file_path,"rb") )



  key=token['oauth_token']
  secret=token['oauth_token_secret']


  #  Now lets create an access-token (expires in 1hr)
  #
  
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  token = oauth.Token(key,secret)

  # Setup the URL according to Google's XOAUTH implementation. Be sure
  # to replace the email here with the appropriate email address that
  # you wish to access.

  myurl = "https://mail.google.com/mail/b/%s/imap/" %  user_email_address.strip()

  print myurl
  conn = imaplib.IMAP4_SSL('imap.googlemail.com')
  conn.debug = 4 

  # This is the only thing in the API for impaplib.IMAP4_SSL that has 
  # changed. You now authenticate with the URL, consumer, and token.
  conn.authenticate(myurl, consumer, token)

  # Once authenticated everything from the impalib.IMAP4_SSL class will 
  # work as per usual without any modification to your code.
  # conn.select('INBOX')
  # print conn.list()

  import gmail_api as gmail

  gm = gmail.GAccount(conn)
  mboxes = gm.getMboxes()
  print mboxes

  mboxName = None 
  while mboxName not in mboxes.keys():
    mboxName = raw_input('Which mbox ?')

  gmbox = mboxes[mboxName]
  gmbox.process()
  messages = gmbox.getMessages();
  lenx = len(messages)
  print "Messages (%d) : " % lenx
  print messages
  print "...... "

  
  for msgid, msg in messages.items():
    message = gmbox.getMessage(msg.uid)
    print "Message : " 
    print message
    # print "Body : " 
    # print message.Body



  print "Moving a message to INBOX"
  msgId = None
  while msgId not in messages.keys():
    msgId = raw_input('Which UID to move ?')

  print "Get Mesg"
  msg = gmbox.getMessage(msgId)
  print "Move message"
  gm.moveMessage(msgId, mboxName, "INBOX")



#-------------------------------------------

if __name__ == "__main__":
  sys.exit(main())




