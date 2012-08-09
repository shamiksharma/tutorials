# The Application's credentials
#twitter_consumer_key="Override this in local_settings.py"
#twitter_consumer_secret="Override this in local_settings.py (not checked in)"


twitter_consumer_key="dKSDqSuoV2fZrR0m2vcA"
twitter_consumer_secret="VqBka23WsFCRlp9GDWts5b1P9xeDRvLwLFMfRj4ElGo"

twitter_application_access_levels="rw"

#Twitter APIs
twitter_request_token_url="https://api.twitter.com/oauth/request_token"
twitter_authorize_url="https://api.twitter.com/oauth/authorize"
twitter_access_token_url="https://api.twitter.com/oauth/access_token"


try:
   from local_settings import *
except:
   print "Import Error"
   pass
