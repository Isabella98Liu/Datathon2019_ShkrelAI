# Twitter API test

import twitter

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

api = twitter.Api(consumer_key="EwIs54k4A8rqQh7ddwoxijmLo",
                  consumer_secret="2OwXKwDvs4gz3PgQ0ZREoRv67k9MCObOQAt9eoaCiDPsbNKVXX",
                  access_token_key="1096596922431930368-1GwsadoZjGEQ491BqnBEnEDFttDttc",
                  access_token_secret="Ym94MmzyvYsR5awSiH0WORAxtNwbAYpahWqF2k5HUOuaj")

trump_timeline = get_tweets(api, "realDonaldTrump")
for i in trump_timeline:
    print(i.text)
