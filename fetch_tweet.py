from urllib import response
import tweepy
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
def scrape_tweet(word):
    tweets = tweepy.Cursor(api.search_tweets,
                            word,
                            until = "2022-05-01",
                            lang="en",
                                tweet_mode='extended').items(500)
    db = pd.DataFrame(columns=['username',
                                    'following',
                                    'followers',
                                    'retweetcount',
                                    'text', 'date'])
    
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1

    # we will iterate over each tweet in the
    # list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        date = tweet.user.created_at
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        retweetcount = tweet.retweet_count
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        # Here we are appending all the
        # extracted information in the DataFrame
        ith_tweet = [username, following,
                        followers,
                        retweetcount, text, date]
        db.loc[len(db)] = ith_tweet

        i = i+1
    filename = f'data/scraped_tweets{word}.csv'
    # we will save our database as a CSV file.
    db.to_csv(filename)

if __name__ == '__main__':
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAADxs%2FwAAAAAAIs3jej3TCI0PhuGbMXrnnyJVwoE%3DOGWO0y8ga9qthK7tnzGkQ3oFE6aGBEBaQzVmXJA3xNmn7CpzzF'
    access_token = '838056936423698433-frZyLOgBOYIRVATcERyPzZX3BZYx98o'
    access_token_secret = '7Hp2r4r6kIEdfDJLxoCMffGojHNZrdBybSPYcfH8asuog'
    api_key = 'ikB4Diw0MZQHTNmLsQOu60DGj'
    api_key_secret = 'LxFnbcL1e99rD3MuarP34hDRQdh2aHBNH0J9M2AOfXiGW3Yy1M'

    top_crypto = ['Bitcoin', 'Ethereum', 'XRP', 'Tether',
                'Dogecoin']

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    for crypto in top_crypto:
        scrape_tweet(crypto)
        print (f'Done with {crypto}')
        print ("-------------------")