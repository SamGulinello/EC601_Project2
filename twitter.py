import yaml
import requests
from requests.auth import HTTPBasicAuth

# Load API Key Info
with open("creds/api-keys.yml") as f:
    data = yaml.safe_load(f)

# Define Global Variables
API_KEY = data["Twitter"]["apiKey"]
API_SECRET = data["Twitter"]["apiSecret"]
BEARER_TOKEN = data["Twitter"]["bearerToken"]
BASE_URL = "https://api.twitter.com/2"
headers = {"Authorization": "Bearer {}".format(BEARER_TOKEN)}

def getUserID(username):
    payload = requests.get('{}/users/by?usernames={}'.format(BASE_URL, username), headers = headers)

    if(payload.status_code == 200):
        return payload.json()["data"][0]["id"]
    else:
        raise RuntimeError("Twitter API Returned Code " + str(payload.status_code))

def getUserTweets(id):
    payload = requests.get('{}/users/{}/tweets'.format(BASE_URL, id), headers = headers)
    

def searchTweets(topic, query = ""):
    payload = requests.get('https://api.twitter.com/2/tweets/search/recent?query={}{}'.format(topic, query), headers = headers)
    
    return payload.json()