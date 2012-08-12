
YAHOO_CONSUMER_KEY="Fill This in"
YAHOO_CONSUMER_SECRET="Fill This in"
GMAIL_ADDRESS='your email address'


GOOGLE_CONSUMER_KEY="anonymous"
GOOGLE_CONSUMER_SECRET="anonymous"

token_file_path = "/tmp/ytokens.txt"

GOOGLE_SCOPE="https://mail.google.com/,https://www.googleapis.com/auth/userinfo.email,https://www.googleapis.com/auth/userinfo.profile,https://www.googleapis.com/auth/userinfo.id"

try:
   from local_settings import *  # override consumer_key, secret etc.
except ImportError:
   print "WARNING: No local_settings"
   pass
