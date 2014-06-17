import sys
f=open(sys.argv[1],"r")
review=open(sys.argv[2],"r")
authorinfo=[line.strip().split("\t") for line in f]
authorinfo.pop(0)
loc = "/v/filer4b/v25q009/kk8/nlp/AmazonDataBackup/AuthorIdentification/500authors/"
count=0
authorselected = []
for author in authorinfo:
	try:
		int(author[2])
	except:
		continue
	if int(author[2])>=500  and int(author[2]) <= 1000:
		authorselected.append(author[0])

reviewinfo=[line.strip().split("\t") for line in review]
count=0
for info in reviewinfo:
	for author in authorselected:
		if  author in info[0]:
			f = open(loc+info[0], "a")
			try:
				len(info[7])
			except:
				print "bad file\n"
				continue
			count+=1
			print count
			f.write(info[7]+"\n")		
			f.close()
			break
					
