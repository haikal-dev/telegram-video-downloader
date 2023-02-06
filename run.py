#!/bin/python3

from telethon import TelegramClient, events, sync

api_id = 123456
api_hash = 'abc12345'
phone_number = '+60134567890'

#client = TelegramClient('my', api_id, api_hash)
#client.start()

with TelegramClient('name', api_id, api_hash) as client:
    #client.send_message('me', 'Hello, myself!')
    #result = client.download_profile_photo('me')
    #print(result)
    #print(client.get_me().stringify())
    messages = client.get_messages('Projek_high_council_cir')
    print(messages)
    #messages[0].download_media()
