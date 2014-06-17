import sys
import nltk

f = open(sys.argv[1], "r")
reviewdata= [line.strip().split("\t") for line in f]

for reviewdatum in reviewdata:
    try:
        len(reviewdatum[11])
    except:
        reviewdata.remove(reviewdatum)
reviewdata.pop(0)
print len(reviewdata)
##-----bigram to find duplicate------#
for i in range(len(reviewdata)/2):
    for j in range(i, len(reviewdata)/2):
        if i != j:
            sent1 = reviewdata[i][11].split(" ")
            sent2 = reviewdata[j][11].split(" ")
            commonbigram = set(nltk.bigrams(sent1)) & set(nltk.bigrams(sent2))
            if len(commonbigram) >= 0.5*len(sent1) or len(commonbigram)>= 0.5*len(sent2):
                if reviewdata[i][1] == reviewdata[j][1] and reviewdata[i][5] == reviewdata[i][5]:
                    continue
                else:
                    print reviewdata[i], reviewdata[j]
