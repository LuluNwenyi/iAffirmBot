import random
import time
import json
import requests
import tweepy
import os


consumer_key = os.environ.get('API_KEY')
consumer_secret_key = os.environ.get('API_SECRET_KEY')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')


def get_affirmations():
    response = requests.get('https://iaffirm.herokuapp.com/affirmations').text
    affirmation = json.loads(response)
    return (affirmation["affirmations"])



def get_random_affirmation():
    affirmations = get_affirmations()
    random_affirmation = random.randint(0, len(affirmations) - 1)
    return (affirmations[random_affirmation]['text'])


def create_tweet():
    affirmation = get_random_affirmation()
    tweet = (affirmation)
    return tweet
    

def tweet_quote():

    interval = 60 * 5
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    while True:
        try:
            tweet = create_tweet()
            api.update_status(tweet + " #iAffirm")
            time.sleep(interval)
        except tweepy.TweepError as e:
            print(e.reason)
        

if __name__ == "__main__":
    tweet_quote() 
   