from textblob import TextBlob
import tweepy
test = TextBlob("Vis needs a full time role in Data Science")

print(test.tags,test.words)


Consumer_Key =	'yourkey'
Consumer_Secret = 'yourkey'

Access_Token = 'yourkey'
Access_Token_Secret	= 'yourkey'

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

twitter_api = tweepy.API(auth)

public_tweets = twitter_api.search('Bill Gates')

for r in public_tweets:
    print(r.text)
    senti = TextBlob(r.text)
    print(senti.sentiment)
