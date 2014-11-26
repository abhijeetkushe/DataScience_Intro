import sys
import json


def main():
    tweet_file = open(sys.argv[1])

    hashtag_count = {}
    scores = {} # initialize an empty dictionary

    for tweet in tweet_file:
        pytweet = json.loads(tweet) 
        if 'entities' in pytweet and pytweet['entities']['hashtags'] is not None:
            for hashtag in pytweet['entities']['hashtags']:
                if hashtag in hashtag_count.iteritems():
                   hashtag_count[hashtag['text']] += hashtag_count[hashtag['text']] + 1
                else:
                   hashtag_count[hashtag['text']] = 1

    hashtag_count_list = []
    for hashtag, count in hashtag_count.iteritems():  
        hashtag_count_list.append((hashtag,count ))

    i = 0
    for hashtag, count in sorted(hashtag_count_list, key=lambda hashCount: hashCount[1], reverse=True):     
        if i < 10:
           print  hashtag.encode('utf-8') + " "+str(count)
           i+=1
        elif i == 10:
           break 
           
        


if __name__ == '__main__':
    main()
