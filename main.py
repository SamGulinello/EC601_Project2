import twitter
import googleNLP as google

class tweet ():
    def __init__(self, text = "", userID = ""):
        self.text = text
        self.userID = userID
        self.sentiment = self.getSentiment()

    def getSentiment(self):
        sentiment = google.analyze_text_sentiment(self.text)
        return sentiment["score"]

def main():
    username = "business"
    tweets = twitter.getUserTweets(twitter.getUserID(username))
    

if(__name__ == "__main__"):
    main()