from textblob import TextBlob
import tweepy
test = TextBlob("Vis needs a full time role in Data Science")

print(test.tags,test.words)


Consumer_Key =	'QN0HG8XpgI2zchl6AhPlgjj5g'
Consumer_Secret = '8W9tRf690MIZC1tFg6hgX7fgQrKIe4IoMDD6XRuERUziAFJAKO'

Access_Token = '1014715995619856384-GabIqcy1PzI4mbPp6Au461jbRrofDP'
Access_Token_Secret	= 'k4GMY7d9RYwDTrJNgAXYNetbAXw7LyM4VsvVJ6bjQCMSm'

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

twitter_api = tweepy.API(auth)

public_tweets = twitter_api.search('Bill Gates')

for r in public_tweets:
    print(r.text)
    senti = TextBlob(r.text)
    print(senti.sentiment)