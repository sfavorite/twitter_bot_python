#!/usr/bin/env python

from twython import Twython
from twython import TwythonStreamer
from dotenv import load_dotenv, find_dotenv
import random
import os


# List of messages to choose from
messages = [
    "Hello",
    "Bye",
    "Okay",
    "AI overlords"
]

# Load key, token, secrets from .env
load_dotenv(find_dotenv())

# Twitter keys, etc we need
consumer_key        = os.environ.get("consumer_key")
consumer_secret     = os.environ.get("consumer_secret")
access_token        = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# First message
message = 'Hi'

# Send a twitter message
#twitter.update_status(status=message)

# Message to post
message = "Nature"

# Picture to post
photo = open("nature.jpg", 'rb')

# Post message with media
#twitter.update_status_with_media(status=message, media=photo)
#print("Sent: {}".format(message));

#message = random.choice(messages)

# Create a TwythonStreamer to read tweets
class TwyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@{}: {}".format(username, tweet))
#        if 'text' in data:
#            print(data['text'])

stream = TwyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='@realDonaldTrump')
