import requests
import json
import oauth2
import os

def encode_search(search_text):
    return search_text.replace(' ','%20')

# api end-point
retweet_endpoint  = "https://api.twitter.com/1.1/search/tweets.json?q=power%20rangers&result_type=popular"
#result_type: popular,recent,mixed

print(retweet_endpoint)
params = {"q":"sorteio jantar"}

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

request = oauth2.Request(parameters = params)


response,data = client.request(retweet_endpoint,
                              'GET')


#print(data.decode('utf8').replace("'", '"'))
json_data = json.loads(data.decode('utf8'))

'''
json_data keys:
created_at
id
id_str
text
truncated
entities
extended_entities
metadata
source
in_reply_to_status_id
in_reply_to_status_id_str
in_reply_to_user_id
in_reply_to_user_id_str
in_reply_to_screen_name
user
geo
coordinates
place
contributors
retweeted_status
is_quote_status
retweet_count
favorite_count
favorited
retweeted
possibly_sensitive
lang
'''

for i,status in enumerate(json_data['statuses']):
    print(str(i) + "::" + status['id_str'] + "::" + status['text'])
