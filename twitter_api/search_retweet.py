import requests
import json
import oauth2
import os
import time

def encode_search(search_text):
    return search_text.replace(' ','%20')

class Retweeter:
    def __init__(self,
                  consumer_key,
                  consumer_key_secret,
                  access_token,
                  access_token_secret,
                  result_type="popular"):
        self.__end_point_url_search__ = "https://api.twitter.com/1.1/search/" \
                                        "tweets.json?"
        self.__end_point_url_retweet__ = "https://api.twitter.com/1.1/" \
                                         "statuses/retweet/"
        self.__sleep_time__ = 3

        self.__result_type__ = result_type#result_type: popular,recent,mixed
        self.__ids_to_retweet__ = []
        consumer = oauth2.Consumer(key = consumer_key,
                                  secret=consumer_key_secret)
        access_token = oauth2.Token(key=access_token,
                                    secret=access_token_secret)

        self.__client__ = oauth2.Client(consumer,
                                        access_token)


    def __search__(self,search_text):
        url = self.__get_search_url__(search_text)
        response,data = self.__client__.request(url,
                                                'GET')
        statuses = self.__convert_data_to_json__(data)['statuses'] #add try get
        for status in statuses:
            print(status["text"])
            self.__ids_to_retweet__.append(status["id_str"])

        return

    @staticmethod
    def __convert_data_to_json__(data):
        return json.loads(data.decode('utf8'))

    def __retweet__(self):
        for id in self.__ids_to_retweet__:
            time.sleep(self.__sleep_time__)
            url = self.__get_retweet_url__(id)
            response,data = self.__client__.request(url,
                                    'POST')
            time.sleep(self.__sleep_time__)

    def __get_retweet_url__(self,id):
        return self.__end_point_url_retweet__ + str(id) + ".json"

    def __get_search_url__(self,search_text):
        search_text_encoded = search_text.replace(' ','%20')
        result = "%sq=%s&result_type=%s"\
        %(self.__end_point_url_search__ ,search_text_encoded, self.__result_type__)
        return result

    def run(self,search_text):
        self.__search__(search_text)
        self.__retweet__()




if __name__ == "__main__":
    folder_path = os.path.dirname(__file__)
    keys_file_path = os.path.join(folder_path,
                                  "../keys.json")
    with open(keys_file_path) as f:
        keys = json.load(f)

    my_retweeter = Retweeter(keys['twitter']['consumer_key'],
                             keys['twitter']['consumer_key_secret'],
                             keys['twitter']['access_token'],
                             keys['twitter']['access_token_secret'])
    my_retweeter.run("sorteio")
