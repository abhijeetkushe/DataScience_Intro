import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def sentiment(tweet, scores, scorescomp):
    score = 0
    outliers = []
    for word in tweet.split():
        if word in scores:
           score = score + scores[word]  
        else:
            outliers.append(word)
    for word in outliers:
    	if word in scorescomp:
           scorescomp[word] = scorescomp[word] + score 
        else:
           scorescomp[word] = score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score) # Convert the score to an integer.
    tweets = [] # initialize an empty array
    scorescomp = {}
    for tweet in tweet_file:
        pytweet = json.loads(tweet)	
        if 'text' in pytweet:
            sentiment(pytweet['text'],scores, scorescomp)     
    for word,score in scorescomp.iteritems():
    	sentimentScore = str(float(score/len(scorescomp)))
        print word.encode('utf-8') +" "+sentimentScore       
        

if __name__ == '__main__':
    main()
