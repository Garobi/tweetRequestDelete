import datetime
import json
import authDataDelete
import requests

def deleteTweet(tweet):
    requests.post(
        'https://x.com/i/api/graphql/VaenaVgh5q5ih7kvyVjgtg/DeleteTweet',
        cookies=authDataDelete.cookies,
        headers=authDataDelete.headers,
        json={
            'variables': {
                'tweet_id': tweet['tweet']['tweet_id'],
                'dark_request': False,
            },
            'queryId': 'VaenaVgh5q5ih7kvyVjgtg',
        },
    )
    requests.post(
        'https://x.com/i/api/graphql/iQtK4dl5hBmXewYZuEOKVw/DeleteRetweet',
        cookies=authDataDelete.cookies,
        headers=authDataDelete.headers,
        json={
            'variables': {
                'tweet_id': tweet['tweet']['tweet_id'],
                'dark_request': False,
            },
            'queryId': 'iQtK4dl5hBmXewYZuEOKVw',
        },
    )
    
f = open("tweet-headers.js", "r")
data_string = f.read()
json_data = data_string.split('= ')[1]
tweets = json.loads(json_data)

date_format = "%a %b %d %H:%M:%S %z %Y"

last_month_naive = datetime.datetime.now() - datetime.timedelta(days=30)

last_month = last_month_naive.replace(tzinfo=datetime.timezone.utc)

for tweet in tweets:
    created_at = datetime.datetime.strptime(tweet['tweet']['created_at'], date_format)
    if created_at < last_month:
        deleteTweet(tweet)