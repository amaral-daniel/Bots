import requests
import json
import oauth2
import os

# api end-point
#Retweets my hello world status

#limit is 300/3 hours
tweet_id = "1214228959929470976" #obtained in response of update request
retweet_endpoint  = "https://api.twitter.com/1.1/statuses/retweet/%s.json" % tweet_id

folder_path = os.path.dirname(__file__)
keys_file_path = os.path.join(folder_path,
                              "../keys.json")

with open(keys_file_path) as f:
    keys = json.load(f)


consumer = oauth2.Consumer(key = keys['twitter']['consumer_key'],
                          secret=keys['twitter']['consumer_key_secret'])
access_token = oauth2.Token(key=keys['twitter']['access_token'],
                            secret=keys['twitter']['access_token_secret'])
client = oauth2.Client(consumer,
                       access_token)


response,data = client.request(retweet_endpoint,
                              'POST')
                             # request.to_postdata())



print(response)
print(data)
