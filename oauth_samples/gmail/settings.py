# The Application's credentials

#Gmail APIs

request_token_url="https://www.google.com/accounts/OAuthGetRequestToken"
authorize_url="https://www.google.com/accounts/OAuthAuthorizeToken"
access_token_url="https://www.google.com/accounts/OAuthGetAccessToken"

consumer_key = "anonymous"
consumer_secret = "anonymous"

token_file_path = "/tmp/tokens.txt"

try:
  from local_settings import *
except:
  print "Import Error for local_settings"
  pass
