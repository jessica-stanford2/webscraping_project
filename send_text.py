import keys

from twilio.rest import Client

client = Client(keys.AccountSID, keys.authtoken)

TwilioNumber = '+18559976167'

myCellPhone = '+18322852232'

message = 'Hi there dude!'

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body= message)

print(textmessage.status)


call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml", to=myCellPhone, from_= TwilioNumber)
