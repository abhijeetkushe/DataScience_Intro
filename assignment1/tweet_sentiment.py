import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def sentiment(tweet, scores):
    score = 0
    for word in tweet.split():
    	if word in scores:
           score = score + scores[word]   
    if score > 0:
       print score
    else:
       print -1        


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score) # Convert the score to an integer.
    tweets = [] # initialize an empty array
    for tweet in tweet_file:
    	pytweet = json.loads(tweet)	
    	if 'text' in pytweet:
    	   sentiment(pytweet['text'],scores)
    	else:
    	   print -1  

if __name__ == '__main__':
    main()
