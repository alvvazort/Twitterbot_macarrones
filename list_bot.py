import tweepy, time
from access import *
from random import randint, random

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

def get_tweets(bot):

    followingIds=bot.get_friend_ids()
    print("followingIds: "+ str(followingIds))

    tweetlist = ["Hola twitter",
                "solo pido q este verano sea mejor q el del año pasado",
                "solo quiero pasar pagina",
                "dar dos besos❌❌❌❌❌❌❌❌\ndar un abrazo✅✅✅✅✅✅✅✅"]
    
    for userId in followingIds:
        time_line=bot.user_timeline(user_id=userId, count=200, include_rts=False, tweet_mode= 'extended')
        
        for info in time_line[10:200]:
            tweetlist.append(info.full_text)
                
    return tweetlist

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()
    
    # Set tweet list:
    tweetlist = get_tweets(bot)

    # Tweet posting:
    while True:
        tweet=tweetlist[randint(0,len(tweetlist)-1)]

        # Print tweet:
        print(tweet)

        # Try to post tweet:
        try:
            print("posting: "+ tweet)
            bot.update_status(tweet)
            print("succesfully posted")
        except tweepy.TwitterServerError as e:
            print("Error: "+e)
            print("Api codes: "+ str(e.api_codes))
            print("Api errors: "+str(e.api_errors))
            print("Api messages: "+ str(e.api_messages))

        # Wait till next sentence extraction:
        secs= randint(3000,5000)
        
        print("Tweetteando en "+str(secs)+" segundos.")
        time.sleep(secs)
