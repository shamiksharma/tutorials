
Shows examples of how to use oauth for Twitter, Gmail, Yahoo and Hotmail

You first need to download python-oauth2 from githib
% cd ~/proj/gitlibs
% git clonepython-oauth2 from githib
% cd ~/proj/gitlibs
% git clone  https://github.com/simplegeo/python-oauth2.git


Link to the download library
% cd proj/tutorials/oauth_samples/twitter
% ln -s ~/proj/gitlibs/python-oauth2/oauth2 oauth2


1. Twitter.

Get an App key and app secret from [here](https://dev.twitter.com/apps)
Twitter calls these a consumer_key and consumer_secret
Store these in a local_settings.py file (not checked in)

% python twitter_test.py

Note that the first time you run this, 
- it will pop a browser and
- take you to twitter to do the oauth dance. 
- Twitter will generate a pin
 - you have to enter into the cmd-line prompt
- the app then gets a access_token, which it serialized into a file.
  for many subsequent uses  The access_token is for a (long-lived) session)
- then the access_token is used to fetch the timelinel
- Following requests can reuse the access_token from the file.


2. Gmail oauth



Notes:
- Gmail needs a scope="https://mail.google.com/"  params to get req-token.
  It needs the trailing backslash

- http://developer.yahoo.com/oauth/guide/oauth-auth-flow.html
  is a good illustration

- http://nullinfo.wordpress.com/oauth-yahoo/
  Breaks down the steps very well.


You will need to pip install httplib2.
Its easier to use than httplib2, but provides the same func.


ALso look at :
https://github.com/agildehaus/python-oauthmail
