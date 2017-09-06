#!/usr/bin/env python

from twython import Twython
from dotenv import load_dotenv, find_dotenv
import os

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
