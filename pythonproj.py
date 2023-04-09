#ONLINE MESSAGE SENDER
import requests
from requests import request

url='https://www.fast2sms.com/dev/bulkV2'

message='Hello'
number='6362383386,9902920921'
payload=f'sender_id=TXTID&message={message}&route=v3&language=english&numbers={number}'

headers = {
    'authorization':'j2r1luyZfMDGFJASahEb4o0NOVQsYd8cXx65Tip9wWRnLevq7B94EOIGx8j0RbqaJri5zVvsBTAnWCMt',
    'Content-Type':'application/x-www-form-urlencoded'     
}

responses = requests.request("POST",url=url, data=payload, headers =headers)
print(responses.txt)