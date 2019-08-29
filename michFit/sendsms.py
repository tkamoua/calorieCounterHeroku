# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC3ad65f3d59327ec474626839cb27d88b", "cbcc53515a75c44ba8ade1676f524ebf")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+16318851769", 
                       from_="+16312065556", 
                       body="Hello from Python!")