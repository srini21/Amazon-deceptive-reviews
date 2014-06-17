import sys
f = open(sys.argv[1], "r")
reviewdata= [line.strip().split("\t") for line in f]
count=0
myst=[]
for reviewdatum in reviewdata:
	try:
		len(reviewdatum[1])
	except:
		continue
	if reviewdatum[1] == 'AUHG8KSHI529U':
		myst.append(reviewdatum[2])
print myst


