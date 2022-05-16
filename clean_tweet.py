from distutils.command.clean import clean
from fileinput import filename
import random
import sys
import pandas as pd
import preprocessing
import csv
import os

def create_dataset(file_name):
    tweets = preprocessing.getDataFromCSV(f'data/scraped_tweets{file_name}.csv')
    cleaned_tweet = []
    for tweet in tweets:
        cleaned_tweet.append(preprocessing.tweet_cleaning_for_sentiment_analysis(tweet))
    tweet_date = preprocessing.modifyDate(f'data/scraped_tweets{file_name}.csv')
    cleaned_tweet_date = []
    c = 0
    for idx in range(1,len(tweet_date)):
        year = tweet_date[idx].split()[0].split("-")[0]
        #print (year)
        if (year == '2022'):
            c+=1
            cleaned_tweet_date.append(1)
        else:
            cleaned_tweet_date.append(0)
    df = pd.read_csv(f'data/scraped_tweets{file_name}.csv')
    df['text'] = cleaned_tweet[1:]
    df['show'] = cleaned_tweet_date
    # we will save our database as a CSV file.
    df.to_csv(f'cleaned_data/{file_name}.csv')


if __name__ == '__main__':

    top_crypto = ['Bitcoin', 'Ethereum', 'XRP', 'Tether',
                'Dogecoin']
    for crypto in top_crypto:
        create_dataset(crypto)
        print (f'Done with {crypto}')
        print ("-------------------")
