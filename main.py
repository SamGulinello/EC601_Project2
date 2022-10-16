import twitter
import googleNLP as google

def p2f(value):
    if(value != None):
        return float(value.strip("%")) / 100
    else:
        return 0.0

def produceOutput(sentiment, company, topTweet):
    print("-" * 8 + " RESULTS " + "-" * 8)
    print("Target Company -> {}".format(company))
    print("-" * 23)
    print("Average Sentiment -> {}".format(sentiment))
    if(sentiment >= 0.06):
        print("Buy Rating -> BUY")
    elif(-0.06 <= sentiment < 0.06):
        print("Buy Rating -> HOLD")
    else:
        print("Buy Rating -> SELL")
    print("-" * 23)
    print("Top Tweet")
    print(topTweet.text)

def main():
    company = input("Enter Company Name Here -> ")

    tweets = twitter.searchTweets(topic = company, params="&max_results=100&tweet.fields=public_metrics")

    total = 0
    topTweet = tweets[0]
    for tweet in tweets:
        if(tweet.retweets > topTweet.retweets):
            topTweet = tweet

        weightedValue = p2f(tweet.sentiment['score']) * p2f(tweet.sentiment['magnitude'])
        total += weightedValue
    
    avg = total / len(tweets)
    
    produceOutput(sentiment = avg, company = company, topTweet = topTweet)

if(__name__ == "__main__"):
    main()