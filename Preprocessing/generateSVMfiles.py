import sys
import random

pos = open(sys.argv[1], "r")
unv = open(sys.argv[2], "r")
posdata = [line for line in pos]
unvdata = [line for line in unv]
newdata = []
#testdata = []
#select = random.sample(posdata, 3000)
#test = list(set(posdata) - set(select))
#for data in select:
#    newdata.append(data)
#
#for data in test:
#    testdata.append(data)

select = random.sample(unvdata, 2000)
for data in unvdata:
    newdata.append(data)

random.shuffle(newdata)
new = open(sys.argv[3],"w")
for line in newdata:
    new.write(str(line))

#new = open(sys.argv[4], "w")
#for line in testdata:
#    new.write(str(line))
