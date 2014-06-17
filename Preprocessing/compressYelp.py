from os import listdir
from os.path import isfile, join
import sys
positivefile="/v/filer4b/v25q009/kk8/nlp/op_spam_v1.4/positive_polarity/deceptive_from_MTurk/fold"
negativefile="/v/filer4b/v25q009/kk8/nlp/op_spam_v1.4/negative_polarity/deceptive_from_MTurk/fold"
allfile = []
for i in range(1,6):
    posfile=[ join(positivefile+str(i),f) for f in listdir(positivefile+str(i)) if isfile(join(positivefile+str(i), f)) ]
    negfile=[ join(positivefile+str(i),f) for f in listdir(negativefile+str(i)) if isfile(join(negativefile+str(i), f)) ]
    allfile=allfile+posfile
    allfile=allfile+negfile
reviews=[]
for fl in allfile:
    f = open(fl, "r")
    for line in f:
        line = line.strip()
        reviews.append(line)
newfile=open(sys.argv[1],"w")
for review in reviews:
    newfile.write(review+"\n")
