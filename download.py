#!/bin/python3

# Import required libraries
from telethon import TelegramClient, types, sync

# Initialize the client
api_id = 12345678 # replace with your API ID
api_hash = "abc123" # replace with your API hash
client = TelegramClient('name', api_id, api_hash)

# Start the client
client.start()

# Get the channel entity
channel_username = 'hotstar_movies_disney_plus'
channel_entity = client.get_entity(channel_username)

# Get the messages in the channel
offset_id = 5
limit = 100
all_messages = []
while True:
    messages = client.get_messages(
        entity=channel_entity,
        limit=limit,
        offset_id=offset_id,
    )
    if not messages:
        break
    all_messages.extend(messages)
    offset_id = messages[-1].id

# Download the videos
for message in all_messages:
    #scan all general messages
    print(message)
    print()

    #scan only for messages that contain media documents
    #if message.media and isinstance(message.media, types.MessageMediaDocument):
        #if message.media.document.mime_type == 'video/mp4':
        #if message.media.document.mime_type == 'video/mkv':
            #print(message)

            # start download
            #if message.id == 7973:
            #    client.download_media(message, 'High_Council_EP03.mp4')

# Disconnect the client
client.disconnect()
