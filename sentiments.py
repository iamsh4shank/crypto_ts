from textblob import TextBlob
import preprocessing
import pandas as pd
# importing the required module
import matplotlib.pyplot as plt

def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)

    # set sentiment
    sentiment = None 
    if analysis.sentiment.polarity > 0:
        sentiment = 'positive'
    elif analysis.sentiment.polarity == 0:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'

    return sentiment, analysis.sentiment.polarity

def calc_sentiments(file_name):
    tweets = preprocessing.modifyDate(f'cleaned_data/{file_name}.csv')
    sentiments = []
    for tc in range(1,len(tweets)):
        sentiment, score = get_tweet_sentiment(tweets[tc])
        sentiments.append(score)
    df = pd.read_csv(f'cleaned_data/{file_name}.csv')
    df['sentiments'] = sentiments
    # we will save our database as a CSV file.
    df.to_csv(f'cleaned_data/sentiment_{file_name}.csv')
    return sentiments
def normalise(x):
    z = []
    for i in x:
        z.append((i-min(x))/(max(x)-min(x))*100)
    return z

def calc_profile_score(file_name):
    tweets = preprocessing.get_cumlative_score(f'cleaned_data/sentiment_{file_name}.csv')
    score = []
    for tc in range(1,len(tweets)):
        score.append(int(tweets[tc])/100)
    df = pd.read_csv(f'cleaned_data/sentiment_{file_name}.csv')
    df['profile_score'] = score
    # we will save our database as a CSV file.
    df.to_csv(f'cleaned_data/final_data/{file_name}.csv')
    return score

if __name__ == '__main__':
    top_crypto = ['Bitcoin', 'Ethereum', 'XRP', 'Tether', 'Dogecoin']
    for crypto in top_crypto:
        input_x = []
        input_y = []
        weighted_score = []
        sentiment_score = calc_sentiments(f'{crypto}')
        profile_score = calc_profile_score(f'{crypto}')
        
        n_profile_score = normalise(profile_score)
        for s, p in zip(sentiment_score, n_profile_score):
            if (p>0):
                weighted_score.append(s*p)
            else:
                weighted_score.append(s)
        date_flag, date_list = preprocessing.date_flag(f'cleaned_data/final_data/{crypto}.csv')
        for idx in range(1, len(date_flag)):
            if (date_flag[idx] == '1'):
                input_x.append(date_list[idx].split()[0])
                input_y.append(weighted_score[idx-1])
        x ={}
        for ele in input_x:
            if ele in x:
                x[ele.split("-")[-1]] += input_y[input_x.index(ele)]
            else:
                x[ele.split("-")[-1]] = input_y[input_x.index(ele)]
        x_in = list(x.keys())
        y_in = list(x.values())
        plt.plot(x_in, y_in)
        plt.xlabel('Date')
        plt.ylabel('Score')
        plt.savefig(f'plots/{crypto}.png')
        #plt.show()
        print (f'Done with {crypto}')
        print ("-------------------")


    





    
