import settings
from oauthmail.oauth import Oauth, OauthSession
from oauthmail.yahoo import YahooMail
import sys, traceback
import pickle
import os
import webbrowser


#-----------------------------------

class MyYahooMail(YahooMail):
    def access_persist(self, old_key, key, secret, handle):
        # Code for persisting Yahoo access token to your database
        return

#-----------------------------------


def main(argv=None):
  
  if argv is None:  argv = sys.argv
  cmd = argv[0]

  oauth = Oauth(settings.YAHOO_CONSUMER_KEY, settings.YAHOO_CONSUMER_SECRET)
   
  token_file_path = settings.token_file_path
  have_token = False;
  # Check if we already have a token saved in the filesystem
  if not os.path.exists(token_file_path):
    session = MyYahooMail(oauth, None, None, None)
    verifier_url = session.authorize("oob")
    user_code = punch_auth_code(verifier_url)
    token = session.access(user_code)
    pickle.dump(token, open(token_file_path,"wb"))
  else:
    print 'Found existing tokens'

  token = pickle.load( open(token_file_path,"rb") )
  mail_session = MyYahooMail(oauth, token[0], token[1], token[2])

  # Fetch identifiers of unread mail
  unread_mids = mail_session.mids_unread('inbox')

  # Fetch all Yahoo messages and print subjects to screen
  for mid in unread_mids:
      try:
        msg = mail_session.fetch('inbox', mid)
      except:
        print "Exception in user code:"
        traceback.print_exc(file=sys.stdout)
        
      print msg['subject']


#-------------------------------------------

if __name__ == "__main__":
  sys.exit(main())
