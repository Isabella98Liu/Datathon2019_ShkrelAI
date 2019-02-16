# Twitter API test

import twitter
import nltk
import datetime
import csv

from nltk.sentiment import *

# Returned timeline is a dictionary of the following fields
# 
def get_tweets(api=None, screen_name=None):
    timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
    earliest_tweet = min(timeline, key=lambda x: x.id).id
    print("getting tweets before:", earliest_tweet)

    while True:
        tweets = api.GetUserTimeline(
            screen_name=screen_name, max_id=earliest_tweet, count=200
        )
        new_earliest = min(tweets, key=lambda x: x.id).id

        if not tweets or new_earliest == earliest_tweet:
            break
        else:
            earliest_tweet = new_earliest
            print("getting tweets before:", earliest_tweet)
            timeline += tweets

    return timeline

def calc_find_weight(word):
    if (word.lower() in positive_adjectives):    
        print("Incrementing becasue of ")
        print(word.lower())
        return 1
    if (word.lower() in negative_adjectives):
        print("Decrementing because of ")
        print(word.lower())
        return -1
    return 0

# Associate a positive weight if there are postitive adjectives and some keyword shows up
# Associate a negative weight if there are negative adjectives and some keyword shows up
def calc_weight(keyword, tweet):
    run = 0
    for i in tweet.text.split():
        if not set(keyword).isdisjoint(tweet.text.split()):
            print(tweet.text.split())
            return (tweet.created_at, tweet.text, 
                    nltk.sentiment.util.demo_liu_hu_lexicon(tweet.text))
    return 0

# Calculates a frequency distribution of words
# Associates a word distribution to each tweet, and maybe we can find statistical patterns within that?
def calc_word_dist(timeline, word):
    the_list = []
    for i in timeline:
        the_list.append(calc_weight(word, i))
    return the_list

api = twitter.Api(consumer_key="EwIs54k4A8rqQh7ddwoxijmLo",
                  consumer_secret="2OwXKwDvs4gz3PgQ0ZREoRv67k9MCObOQAt9eoaCiDPsbNKVXX",
                  access_token_key="1096596922431930368-1GwsadoZjGEQ491BqnBEnEDFttDttc",
                  access_token_secret="Ym94MmzyvYsR5awSiH0WORAxtNwbAYpahWqF2k5HUOuaj")
nltk.download('opinion_lexicon')

handle = input("Twitter Handle (without the @)")
keyword_list = []
while len(keyword_list) == 0 or keyword_list[len(keyword_list)-1] != "STOP":
    keyword_list.append(input("Add a keyword (STOP to stop)"))


the_list = calc_word_dist(get_tweets(api, handle), keyword_list)

with open('filename.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(the_list)

