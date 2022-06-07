from concurrent.futures import thread
import tweepy, time, threading
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

    tweetlist = []
    
    for userId in followingIds:
        time_line=bot.user_timeline(user_id=userId, count=200, include_rts=False, tweet_mode= 'extended')
        
        for info in time_line[10:200]:
            tweetlist.append(info.full_text)
                
    return tweetlist

def tweetMacarrones(bot):
     # Set tweet list:
    tweetlist = get_tweets(bot)

    # Tweet posting:
    while True:
        tweet=tweetlist[randint(0,len(tweetlist)-1)]

        # Print tweet:
        print(tweet)

        # Try to post tweet:
        try:
            if("@" not in tweet):
                print("posting: "+ tweet)
                bot.update_status(tweet)
                print("succesfully posted")
            else:
                print("El tweet tiene una mención, mejor no liarla con las menciones")
                break

        except tweepy.TwitterServerError as e:
            print("Error: "+e)
            print("Api codes: "+ str(e.api_codes))
            print("Api errors: "+str(e.api_errors))
            print("Api messages: "+ str(e.api_messages))

        # Wait till next sentence extraction:
        secs= randint(1000,4000)
        
        print("Tweetteando en "+str(secs)+" segundos.")
        time.sleep(secs)
    
    print("Reiniciando tweetMacarrones")
    tweetMacarrones(bot)

def respondCecyArmy(bot):

    time_line=bot.user_timeline(screen_name="ceciarmy", count=1, include_rts=False, tweet_mode= 'extended')

    for info in time_line:
        tweetId= info.id
        media=chooseImage(bot)
        bot.update_status(status="",media_ids=[media.media_id], in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)
        print("Tweetteando primeros 'Que buen meme de cecyArmy joder'")
    
    while True:

        time_line=bot.user_timeline(screen_name="ceciarmy", since_id= tweetId, include_rts=False, tweet_mode= 'extended')
        print(time_line)
        for info in time_line:
            tweetId= info.id
            media=chooseImage(bot)
            bot.update_status(status="",media_ids=chooseImage(bot), in_reply_to_status_id = tweetId , auto_populate_reply_metadata=True)
            print("Tweetteando 'Que buen meme de cecyArmy joder'")

        secs=600
        print("Se comprobará si ceciArmy ha tweeteado en 10 minutos")
        time.sleep(secs)

def chooseImage(bot):
    listImages=["eciarmy1.jpg","eciarmy2.jpg","eciarmy3.jpg"]
    image= listImages[randint(0,len(listImages)-1)]
    return bot.media_upload("imagenes\c"+image)

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()
    simplethread=[]
    simplethread.append(threading.Thread(target=tweetMacarrones,args=[bot]))
    simplethread.append(threading.Thread(target=respondCecyArmy,args=[bot]))
    
    for i in range(0,len(simplethread)):
        simplethread[i].start()

   
