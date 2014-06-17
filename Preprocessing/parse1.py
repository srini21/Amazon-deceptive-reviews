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
for i in range(len(reviewdata)):
    for j in range(i, len(reviewdata)):
        if i != j:
            sent1 = reviewdata[i][11].split(" ")
            sent2 = reviewdata[j][11].split(" ")
            sent1bigram = set(nltk.bigrams(sent1))
            sent2bigram = set(nltk.bigrams(sent2))
            intersection = set.intersection(sent1bigram,sent2bigram)
            union = set.union(sent1bigram,sent2bigram)
            if len(sent1bigram) <= 3 or len(sent2bigram) <=3:
                continue
            commonbigram = sent1bigram & sent2bigram
            if len(intersection) >= 0.9*len(union):
                if reviewdata[i][1] == reviewdata[j][1] and reviewdata[i][5] == reviewdata[i][5]:
                    continue
                else:
                    print reviewdata[i], reviewdata[j]
