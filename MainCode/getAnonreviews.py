import sys
rfile=open(sys.argv[1],"r")
newfile=open(sys.argv[2],"w")
rdata=[line.strip().split("\t") for line in rfile]
anonAuthors=['A2BB4DGBRVG','A1AQKVKYUF8','A1XGEKIXNRQ','A1D3NBGL55L','A2HOI4FW3RW','A291YTUZVJ7','AWO952G677A','A2PCORE09BP','A2GPLOLLE6B']
for review in rdata:
	for author in anonAuthors:
		if author in review[0]:
			newfile.write(review[0]+"\t"+review[7]+"\n")
			break
