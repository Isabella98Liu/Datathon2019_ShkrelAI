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

def liu_hu_lexicon(sentence, plot=False):
    """
    Basic example of sentiment classification using Liu and Hu opinion lexicon.
    This function simply counts the number of positive, negative and neutral words
    in the sentence and classifies it depending on which polarity is more represented.
    Words that do not appear in the lexicon are considered as neutral.
    :param sentence: a sentence whose polarity has to be classified.
    :param plot: if True, plot a visual representation of the sentence polarity.
    """
    from nltk.corpus import opinion_lexicon
    from nltk.tokenize import treebank

    tokenizer = treebank.TreebankWordTokenizer()
    pos_words = 0
    neg_words = 0
    tokenized_sent = [word.lower() for word in tokenizer.tokenize(sentence)]

    x = list(range(len(tokenized_sent)))  # x axis for the plot
    y = []

    for word in tokenized_sent:
        if word in opinion_lexicon.positive():
            pos_words += 1
            y.append(1)  # positive
        elif word in opinion_lexicon.negative():
            neg_words += 1
            y.append(-1)  # negative
        else:
            y.append(0)  # neutral

    if pos_words > neg_words:
        return 1
    elif pos_words < neg_words:
        return -1
    elif pos_words == neg_words:
        return 0

# Associate a positive weight if there are postitive adjectives and some keyword shows up
# Associate a negative weight if there are negative adjectives and some keyword shows up
def calc_weight(keyword, tweet):
    run = 0
    for i in tweet.text.split():
        if not set(keyword).isdisjoint(tweet.text.split()):
            print(tweet.text.split())
            return (tweet.created_at, tweet.text, liu_hu_lexicon(tweet.text));
    return (0, "", 0)

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

with open('filename.csv', 'w+') as outfile:
    for entries in the_list:
        if entries[0] == 0:
            continue
        outfile.write("%s" % str(entries[0]));
        outfile.write(",");
        outfile.write("%s" % str(entries[1]));
        outfile.write(",");
        outfile.write("%s" % str(entries[2]));
        outfile.write("\n");
