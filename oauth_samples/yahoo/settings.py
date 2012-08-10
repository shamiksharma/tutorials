
YAHOO_CONSUMER_KEY="Fill This in"
YAHOO_CONSUMER_SECRET="Fill This in"

try:
    from local_settings.py import *  # override consumer_key, secret etc.
except ImportError:
    print "WARNING: No local_settings"
    pass
