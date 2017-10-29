import json
import os
from twilio.rest import Client
print(os.getcwd())
with open('secrets.json') as config:
    jsondata = json.load(config)
    ACCOUNT_SID=jsondata["twilio"]["ACCOUNT_SID"]
    AUTH_TOKEN=jsondata["twilio"]["AUTH_TOKEN"]

client = Client(ACCOUNT_SID, AUTH_TOKEN)
numbers = client.available_phone_numbers("US").local.list(area_code="612")


for number in numbers:
    print(number.phone_number)
          
new_message = client.messages.create(to='+16124242328', from_='+19522361481', body='Twilio rocks!')
print('Sending an example message...')

