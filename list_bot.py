import tweepy, time
from access import *
from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()

    # Set waiting time:
    secs = 3

    # Set tweet list:
    tweetlist = ["Hola twitter",
                "solo pido q este verano sea mejor q el del año pasado",
                "solo quiero pasar pagina",
                "dar dos besos❌❌❌❌❌❌❌❌\ndar un abrazo✅✅✅✅✅✅✅✅"]

    # Tweet posting:
    for tweet in tweetlist:
        # Print tweet:
        print(tweet)

        # Try to post tweet:
        try:
            print("posting: "+ tweet)
            bot.update_status(tweet)
            print("succesfully posted")
        except tweepy.TwitterServerError as e:
            print("Error: "+e)
            print("Api codes: "+e.api_codes)
            print("Api errors: "+e.api_errors)
            print("Api messages: "+e.api_messages)

        # Wait till next sentence extraction:
        time.sleep(secs)
