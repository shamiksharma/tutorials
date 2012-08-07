import settings
import urlparse
import oauth2 as oauth
import time
import pickle
import os
import webbrowser

consumer_key = settings.twitter_consumer_key
consumer_secret = settings.twitter_consumer_secret

request_token_url = 'http://twitter.com/oauth/request_token'
access_token_url = 'http://twitter.com/oauth/access_token'
authorize_url = 'http://twitter.com/oauth/authorize'


#-------------------------------------------
def oauth_gen_token():
  consumer = oauth.Consumer(consumer_key, consumer_secret)
  client = oauth.Client(consumer)

  # Step 1: Get a request token. This is a temporary token that is used for 
  # having the user authorize an access token and to sign the request to obtain 
  # said access token.

  print request_token_url
  resp, content = client.request(request_token_url, "GET")
  if resp['status'] != '200':
      raise Exception("Invalid response %s." % resp['status'])

  request_token = dict(urlparse.parse_qsl(content))

  print "Request Token:"
  print "    - oauth_token        = %s" % request_token['oauth_token']
  print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
  print 

  # Step 2: Redirect to the provider. Since this is a CLI script we do not 
  # redirect. In a web application you would redirect the user to the URL
  # below.
  auth_url = "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])

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
  token = oauth.Token(request_token['oauth_token'],
      request_token['oauth_token_secret'])
  token.set_verifier(oauth_verifier)
  client = oauth.Client(consumer, token)

  resp, content = client.request(access_token_url, "POST")
  access_token = dict(urlparse.parse_qsl(content))

  print "Access Token:"
  print "    - oauth_token        = %s" % access_token['oauth_token']
  print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
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

def main():

  token_file_path = '/tmp/twitter_tokens.txt'
  url = "http://api.twitter.com/1/statuses/home_timeline.json"
  have_token = False;

  # Check if we already have a token saved in the filesystem

  if not os.path.exists(token_file_path):
    user_token = oauth_gen_token()
    pickle.dump( user_token, open(token_file_path,"wb"))
  else:
    print 'Found existing tokens'
  
  user_token = pickle.load( open(token_file_path,"rb"))

  key=user_token['oauth_token']
  secret=user_token['oauth_token_secret']


  content = oauth_request (url, key, secret, consumer_key, consumer_secret)
  
  print content

#-------------------------------------------

if __name__ == "__main__":
  main()








