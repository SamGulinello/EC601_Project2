import yaml
import requests
from requests.auth import HTTPBasicAuth
import googleNLP as google
import botometer

# Load API Key Info
with open("creds/api-keys.yml") as f:
    data = yaml.safe_load(f)

# Define Global Variables
API_KEY = data["Twitter"]["apiKey"]
API_SECRET = data["Twitter"]["apiSecret"]
BEARER_TOKEN = data["Twitter"]["bearerToken"]
BASE_URL = "https://api.twitter.com/2"
BOTOMETER_API_KEY = data["Botometer"]["apiKey"]

# Define twitter request headers
headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

# Initialize botometer
twitter_auth = {
    'consumer_key': API_KEY,
    'consumer_secret': API_SECRET
}
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=BOTOMETER_API_KEY,
                          **twitter_auth)

class tweet ():
    def __init__(self, data, userID):
        self.text = data["text"]
        self.userID = userID
        self.ID = data["id"]
        self.retweets = data["public_metrics"]["retweet_count"]
        self.data = data

        try:
            self.sentiment = self.getSentiment()
        except:
            self.sentiment = {"score": None, "magnitude": None}

    def getSentiment(self):
        sentiment = google.analyze_text_sentiment(self.text)
        return sentiment

def getBotometerScore():
    result = bom.check_account('@clayadavis')
    
    return result.json()

def getUserID(username):
    payload = requests.get('{}/users/by?usernames={}'.format(BASE_URL, username), headers = headers)

    if(payload.status_code == 200):
        return payload.json()["data"][0]["id"]
    else:
        raise RuntimeError("Twitter API Returned Code " + str(payload.status_code))

def getUserTweets(id):
    payload = requests.get('{}/users/{}/tweets'.format(BASE_URL, id), headers = headers).json()

    tweetList = []
    for t in payload["data"]:
        n = tweet(t, id)
        tweetList.append(n)

    return tweetList

def searchTweets(topic, params = ""):
    payload = requests.get('https://api.twitter.com/2/tweets/search/recent?query={}{}'.format(topic, params), headers = headers).json()
    tweetList = []
    for t in payload["data"]:
        n = tweet(t, id)
        tweetList.append(n)

    return tweetList