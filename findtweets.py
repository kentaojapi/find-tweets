import json
import csv
import datetime
import os


from requests_oauthlib import OAuth1Session
import slackweb


DEFAULT_TWITTER_API_URL = "https://api.twitter.com/1.1/search/tweets.json"
DEFAULT_SLACK_CHANNEL_URL = os.environ['DEFAULT_SLACK_CHANNEL_URL']
DEFAULT_CSV_FILE = 'keyword.csv'


class FindTweets(object):

    def __init__(self):
        self.CK = os.environ['TWITTER_CONSUMER_KEY']
        self.CS = os.environ['TWITTER_CONSUMER_SECRET']
        self.AT = os.environ['TWITTER_ACCESS_TOKEN_KEY']
        self.AS = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    def load_keywords(self):
        keywords = []
        with open(DEFAULT_CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                keywords.append(row)
        return keywords

    def search(self, keywords, ck, cs, at, As):
        twitter = OAuth1Session(ck, cs, at, As)
        tweets = []
        for keyword in keywords:
            params = {'q': keyword[0], 'count': 50}
            req = twitter.get(DEFAULT_TWITTER_API_URL, params = params)

            if req.status_code == 200:
                search_timeline = json.loads(req.text)
                for tweet in search_timeline['statuses']:
                    if not self.remove_rt(tweet['text']):
                        if tweet['favorite_count'] >= int(keyword[1]):
                            tweet_time = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
                            if self.check_time(tweet_time):
                                tweet_link = 'https://twitter.com/{0}/status/{1}'.format(tweet['user']['screen_name'], tweet['id_str'])
                                tweets.append(tweet_link)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
            else:
                pass
        return tweets

    def remove_rt(self, text):
        if text[0:4] == "RT @":
            return True
        else:
            return False

    def check_time(self, tweet_time):
        now = datetime.datetime.now()
        fifteen_min_before = now - datetime.timedelta(minutes=15)
        day = datetime.date.today()
        day_b15 = datetime.date(tweet_time.year, tweet_time.month, tweet_time.day)
        time = datetime.time(tweet_time.hour, tweet_time.minute, tweet_time.second)
        time_b15 = datetime.time(fifteen_min_before.hour, fifteen_min_before.minute, fifteen_min_before.second)
        if day == day_b15:
            if time > time_b15:
                return True
            else:
                return False
        else:
            return False

    def post_to_slack(self, tweets):
        slack = slackweb.Slack(url=DEFAULT_SLACK_CHANNEL_URL)
        for tweet_link in tweets:
            slack.notify(text=tweet_link)


def lambda_handler(event, context):
    user = FindTweets()
    keywords = user.load_keywords()
    tweets = user.search(keywords, user.CK, user.CS, user.AT, user.AS)
    user.post_to_slack(tweets)
