import sys
import json



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
    tweet_file = open(sys.argv[1])
    totalfreq = 0
    tweets = []
    for tweet in tweet_file:
        pytweet = json.loads(tweet) 
        if 'text' in pytweet:
            tweets.append(pytweet)
            totalfreq =  totalfreq + len(pytweet['text'].split())

    word_occ = {}         

    for pytweet in tweets:
        if 'text' in pytweet:
            words = pytweet['text'].split()
            for word in words:
                if word in word_occ:
                   word_occ[word] = word_occ[word] + 1 
                else:
                   word_occ[word] = 1 

    for word,occ in word_occ.iteritems():
        freq = float(occ/totalfreq)
        print word.encode('utf-8') +" "+str(freq)
        

if __name__ == '__main__':
    main()
