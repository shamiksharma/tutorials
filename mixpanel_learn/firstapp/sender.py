
import sys
import subprocess
import base64
import json

#
# Create a settings.py with
#  token = "YOUR_TOKEN_HERE"
#

import BaseHTTPServer

try:
  import settings 
except ImportError: 
  print "Error : no settings file"
  sys.exit()


def track(event, properties=None):
    """
    A simple function for asynchronously logging to the mixpanel.com API.
    This function requires `curl` and Python version 2.4 or higher.

    @param event: The overall event/category you would like to log this data under
    @param properties: A dictionary of key-value pairs that describe the event
                       See http://mixpanel.com/api/ for further detail.
    @return Instance of L{subprocess.Popen}
    """
    if properties == None:
        properties = {}
    
    if "token" not in properties:
        properties["token"] = settings.token

    params = {"event": event, "properties": properties}
    data = base64.b64encode(json.dumps(params))
    request = "http://api.mixpanel.com/track/?data=" + data
    return subprocess.Popen(("curl",request), stderr=subprocess.PIPE,
        stdout=subprocess.PIPE)


#-----------------------------------------------------------------------
# Start the built-in python httpserver
#

class MainHandler(BaseHTTPServer.BaseHTTPRequestHandler):

  #
  # Writes out the HTTP response and if there is a accesstoken
  # it inserts that into the user-cookie
  #
  def writeResponse(self, content):
    track("test-1", {"pics": "50", "stories": "2"})
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write("<html><body>" + content + "</body></html>")
    return

  def do_GET(self):
    self.writeResponse("Hi")



def main():
# Example usage:
#  print "sent"
  server = BaseHTTPServer.HTTPServer(('', settings.server_port), MainHandler)
  print "Server listening at port http://localhost:" + str(settings.server_port) + "/"
  server.serve_forever()

if __name__ == "__main__":
  main()
