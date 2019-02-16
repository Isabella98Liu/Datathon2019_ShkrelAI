# Twitter API test

import twitter
api = twitter.Api(consumer_key=["EwIs54k4A8rqQh7ddwoxijmLo"],
                  consumer_secret=["2OwXKwDvs4gz3PgQ0ZREoRv67k9MCObOQAt9eoaCiDPsbNKVXX"],
                  access_token_key=["1096596922431930368-1GwsadoZjGEQ491BqnBEnEDFttDttc"],
                  access_token_secret=["Ym94MmzyvYsR5awSiH0WORAxtNwbAYpahWqF2k5HUOuaj"])

api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100")
