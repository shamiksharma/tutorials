import settings
from oauthmail.oauth import Oauth
from oauthmail.yahoo import YahooMail


class MyYahooMail(YahooMail):
    def access_persist(self, old_key, key, secret, handle):
        # Code for persisting Yahoo access token to your database
        return



yahoo_oauth = Oauth(settings.YAHOO_CONSUMER_KEY, settings.YAHOO_CONSUMER_SECRET)
yahoo_mail = MyYahooMail(yahoo_oauth)

# Fetch identifiers of unread mail
unread_yahoo = yahoo_mail.mids_unread('Inbox')

# Fetch all Yahoo messages and print subjects to screen
for mid in unread_yahoo:
    msg = yahoo_mail.fetch('Inbox', mid)
    print msg['subject']
