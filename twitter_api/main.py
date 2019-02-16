# Twitter API test

import twitter
import nltk

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

positive_adjectives = [
"adaptable"
"adventurous"
"affable"
"affectionate"
"agreeable"
"ambitious"
"amiable"
"amicable"
"amusing"
"brave"
"bright"
"broad-minded"
"calm"
"careful"
"charming"
"communicative"
"compassionate"
"conscientious"
"considerate"
"convivial"
"courageous"
"courteous"
"creative"
"decisive"
"determined"
"diligent"
"diplomatic"
"discreet"
"dynamic"
"easygoing"
"emotional"
"energetic"
"enthusiastic"
"exuberant"
"fair-minded"
"faithful"
"fearless"
"forceful"
"frank"
"friendly"
"funny"
"generous"
"gentle"
"good"
"gregarious"
"hard-working"
"helpful"
"honest"
"humorous"
"imaginative"
"impartial"
"independent"
"intellectual"
"intelligent"
"intuitive"
"inventive"
"kind"
"loving"
"loyal"
"modest"
"neat"
"nice"
"optimistic"
"passionate"
"patient"
"persistent"
"pioneering"
"philosophical"
"placid"
"plucky"
"polite"
"powerful"
"practical"
"pro-active"
"quick-witted"
"quiet"
"rational"
"reliable"
"reserved"
"resourceful"
"romantic"
"self-confident"
"self-disciplined"
"sensible"
"sensitive"
"shy"
"sincere"
"sociable"
"straightforward"
"sympathetic"
"thoughtful"
"tidy"
"tough"
"unassuming"
"understanding"
"versatile"
"warmhearted"
"willing"
"witty"
]

negative_adjectives = [
"aggressive"
"aloof"
"arrogant"
"belligerent"
"big-headed"
"bitchy"
"boastful"
"bone-idle"
"boring"
"bossy"
"callous"
"cantankerous"
"careless"
"changeable"
"clinging"
"compulsive"
"conservative"
"cowardly"
"cruel"
"cunning"
"cynical"
"deceitful"
"detached"
"dishonest"
"dogmatic"
"domineering"
"finicky"
"flirtatious"
"foolish"
"foolhardy"
"fussy"
"greedy"
"grumpy"
"gullible"
"harsh"
"impatient"
"impolite"
"impulsive"
"inconsiderate"
"inconsistent"
"indecisive"
"indiscreet"
"inflexible"
"interfering"
"intolerant"
"irresponsible"
"jealous"
"lazy"
"Machiavellian"
"materialistic"
"mean"
"miserly"
"moody"
"narrow-minded"
"nasty"
"naughty"
"nervous"
"obsessive"
"obstinate"
"overcritical"
"overemotional"
"parsimonious"
"patronizing"
"perverse"
"pessimistic"
"pompous"
"possessive"
"pusillanimous"
"quarrelsome"
"quick-tempered"
"resentful"
"risky"
"rude"
"ruthless"
"sarcastic"
"secretive"
"selfish"
"self-centred"
"self-indulgent"
"silly"
"sneaky"
"stingy"
"stubborn"
"stupid"
"superficial"
"tactless"
"timid"
"touchy"
"thoughtless"
"truculent"
"unkind"
"unpredictable"
"unreliable"
"untidy"
"untrustworthy"
"vague"
"vain"
"vengeful"
"vulgar"
"weak-willed"
"wrong"
]

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
    for i in tweet.split():
        if keyword == i:
            run = 1
            break
    if run == 1:
        return (tweet, nltk.sentiment.util.demo_liu_hu_lexicon(tweet, false))
    return 0

# Calculates a frequency distribution of words
# Associates a word distribution to each tweet, and maybe we can find statistical patterns within that?
def calc_word_dist(timeline, word):
    the_list = []
    for i in timeline:
        the_list.append(calc_weight(word, i.text))
    return the_list

api = twitter.Api(consumer_key="EwIs54k4A8rqQh7ddwoxijmLo",
                  consumer_secret="2OwXKwDvs4gz3PgQ0ZREoRv67k9MCObOQAt9eoaCiDPsbNKVXX",
                  access_token_key="1096596922431930368-1GwsadoZjGEQ491BqnBEnEDFttDttc",
                  access_token_secret="Ym94MmzyvYsR5awSiH0WORAxtNwbAYpahWqF2k5HUOuaj")

nltk.download("maxent_treebank_pos_tagger")

trump_timeline = get_tweets(api, "business")
the_list = calc_word_dist(trump_timeline, "a")

for i in the_list:
    print(i)
