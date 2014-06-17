import sys

f = open(sys.argv[1], "r")
reviewdata= [line.strip().split("\t") for line in f]
output=open(sys.argv[2],"w")
for reviewdatum in reviewdata:
	try:
		len(reviewdatum[11])
	except:
		continue	
        if(reviewdatum[2] is '0'):
            for leaf in reviewdatum:
                output.write(leaf+"\t")
            output.write("\n")

            

